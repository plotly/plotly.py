window.genUID = function() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
};

require(["widgets/js/widget"], function(WidgetManager){

    var GraphView = IPython.DOMWidgetView.extend({
        render: function(){
            var that = this;

            var frameId = window.genUID();
            var loadingId = 'loading-'+frameId;


            var _graph_url = that.model.get('_graph_url');

            // variable plotly_domain in the case of enterprise
            var url_parts = _graph_url.split('/');
            var plotly_domain = url_parts[0] + '//' + url_parts[2];

            // Place IFrame in output cell div `$el`
            that.$el.css('width', '100%');
            that.$graph = $(['<iframe id="'+frameId+'"',
                             'src="'+_graph_url+'.embed"',
                             'seamless',
                             'style="border: none;"',
                             'width="100%"',
                             'height="600">',
                             '</iframe>'].join(' '));
            that.$graph.appendTo(that.$el);

            that.$loading = $('<div id="'+loadingId+'">Initializing...</div>')
                            .appendTo(that.$el);

            // initialize communication with the iframe
            if(!('pingers' in window)){
                window.pingers = {};
            }

            window.pingers[frameId] = setInterval(function() {
                that.graphContentWindow = $('#'+frameId)[0].contentWindow;
                that.graphContentWindow.postMessage({ping: true}, plotly_domain);
            }, 200);

            // Assign a message listener to the 'message' events
            // from iframe's postMessage protocol.
            // Filter the messages by iframe src so that the right message
            // gets passed to the right widget
            if(!('messageListeners' in window)){
                 window.messageListeners = {};
            }

            window.messageListeners[frameId] = function(e) {
                if(_graph_url.indexOf(e.origin)>-1) {
                    var frame = document.getElementById(frameId);

                    if(frame === null){
                        // frame doesn't exist in the dom anymore, clean up it's old event listener
                        window.removeEventListener('message', window.messageListeners[frameId]);
                        clearInterval(window.pingers[frameId]);
                    } else if(frame.contentWindow === e.source) {
                        // TODO: Stop event propagation, so each frame doesn't listen and filter
                        var frameContentWindow = $('#'+frameId)[0].contentWindow;
                        var message = e.data;

                        if(message==='pong') {
                            $('#loading-'+frameId).hide();
                            clearInterval(window.pingers[frameId]);
                            that.send({event: 'pong', graphId: frameId});
                        } else if (message.type==='hover' ||
                                   message.type==='zoom'  ||
                                   message.type==='click' ||
                                   message.type==='unhover') {
                            that.send({event: message.type, message: message, graphId: frameId});
                        }
                    }
                }
            };

            window.removeEventListener('message', window.messageListeners[frameId]);
            window.addEventListener('message', window.messageListeners[frameId]);

        },

        update: function() {
            // Listen for messages from the graph widget in python
            var message = this.model.get('_message');

            message = JSON.parse(message);

            var plot = $('#'+message.graphId)[0].contentWindow;
            plot.postMessage(message, 'https://plot.ly');

            return GraphView.__super__.update.apply(this);
        }
    });

    // Register the GraphView with the widget manager.
    WidgetManager.register_widget_view('GraphView', GraphView);
});

//@ sourceURL=graphWidget.js
