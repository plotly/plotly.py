import { IDisposable } from '@phosphor/disposable';
import { ISignal } from '@phosphor/signaling';
/**
 * A class that monitors activity on a signal.
 */
export declare class ActivityMonitor<Sender, Args> implements IDisposable {
    /**
     * Construct a new activity monitor.
     */
    constructor(options: ActivityMonitor.IOptions<Sender, Args>);
    /**
     * A signal emitted when activity has ceased.
     */
    readonly activityStopped: ISignal<this, ActivityMonitor.IArguments<Sender, Args>>;
    /**
     * The timeout associated with the monitor, in milliseconds.
     */
    timeout: number;
    /**
     * Test whether the monitor has been disposed.
     *
     * #### Notes
     * This is a read-only property.
     */
    readonly isDisposed: boolean;
    /**
     * Dispose of the resources used by the activity monitor.
     */
    dispose(): void;
    /**
     * A signal handler for the monitored signal.
     */
    private _onSignalFired(sender, args);
    private _timer;
    private _timeout;
    private _sender;
    private _args;
    private _isDisposed;
    private _activityStopped;
}
/**
 * The namespace for `ActivityMonitor` statics.
 */
export declare namespace ActivityMonitor {
    /**
     * The options used to construct a new `ActivityMonitor`.
     */
    interface IOptions<Sender, Args> {
        /**
         * The signal to monitor.
         */
        signal: ISignal<Sender, Args>;
        /**
         * The activity timeout in milliseconds.
         *
         * The default is 1 second.
         */
        timeout?: number;
    }
    /**
     * The argument object for an activity timeout.
     *
     */
    interface IArguments<Sender, Args> {
        /**
         * The most recent sender object.
         */
        sender: Sender;
        /**
         * The most recent argument object.
         */
        args: Args;
    }
}
