const getHref = (result) => {
    var path = result.file.path;
    if (result && result.meta && result.meta.leadHeading && result.meta.leadHeading.id) {
        path = (path + "#" + result.meta.leadHeading.id);
    }
    if (result && result.meta && result.meta.leadHeading && result.meta.leadHeading.value) {
        path = (path + "#" + result.meta.leadHeading.slug);
    }
    return path;
};
const getLabel = (reference) => {
    var label = reference.meta?.leadHeading?.value || reference.file?.title;
    label = label.replace(/[^\x00-\x7F]/g, "");
    return label;
};

const setCookie = (name, value, days) => {
    const expires = new Date();
    expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
};

const getCookie = (name) => {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return null;
};

const getUniqueID = () => {
    const storedID = getCookie("plotly-chatbot-cookie");

    if (storedID) {
        return storedID;
    } else {
        const newID = generateUniqueID();
        setCookie("plotly-chatbot-cookie", newID, 365);
        return newID;
    }
};

const generateUniqueID = () => {
    return Date.now().toString();
};

window.markprompt = {
    projectKey: 'pk_0upevf7bcscej8JQMALYiqmXoWQkltw3',
    container: '#markprompt',
    options: {
        chat: {
            systemPrompt: "- You are an enthusiastic company representative from Plotly who loves to help people!\\\n- You must never mention a competing product.\\\n- Never give code examples which are not provided in the docs, and don't give code examples in other languages than Python.",
            defaultView: {
                message: "Welcome to Plotly's AI Assistant",
                promptsHeading: 'Popular questions',
                prompts: [
                    'How can I get started with Plotly Express?',
                    'How can I change the color of graph labels?',
                    'How do I move the legend to the top of the graph?',
                    'How can I use Plotly Express with Dash?',
                ],
            },
            conversationMetadata: {
                "userid": getUniqueID(),
                "source": "graphing-library-docs",
            },
            enabled: true,
            model: 'gpt-3.5-turbo',
        },
        search: {
            enabled: false,
            getHref: getHref
        },
        references: {
            heading: 'References',
            getHref: getHref,
            getLabel: getLabel,
        },
        feedback: {
            enabled: true
        },
        trigger: {
            buttonLabel: 'Ask AI',
            iconSrc: '/python/assets/images/markprompt_chat.svg'
        },
        branding: {
            type: 'text'
        }

    }

}