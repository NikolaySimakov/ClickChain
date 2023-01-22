import { ref, reactive, watch } from 'vue';
import { useLinkStore } from '../../stores/links';


export default function useLinkForm(link) {

    const store = useLinkStore();

    const buttonSettings = reactive({
        message: 'Shorten',
        style: 'bg-neutral-400 text-white',
        onClick: null,
    })

    const inputStyle = ref('');

    const isValid = l => {
        let pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
            '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
            '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
            '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
        return !!pattern.test(l);
    };

    watch(link, () => {
        updateButtonSettings();
    });

    const updateButtonSettings = () => {

        // remove all settings
        resetSettings();
        
        // link shortener available
        if (!!link.value && isValid(link.value)) {
            buttonSettings.style = 'bg-emerald-300 text-black';
            buttonSettings.onClick = getShortLink;
        }

        // link copy available / unavailable
        if (!!store.getShortLink && link.value === store.getShortLink) {
            buttonSettings.message = 'Copy';
            buttonSettings.style = 'bg-emerald-300 text-black';
            buttonSettings.onClick = copyShortLink;
        }
    }

    const resetSettings = () => {
        buttonSettings.message = 'Shorten';
        buttonSettings.style = 'bg-neutral-400 text-white';
        buttonSettings.onClick = null;

        if (link.value !== store.getShortLink) {
            inputStyle.value = '';
        }
    }

    const getShortLink = () => {
        store.generateShortLink(link.value).then(() => {
            link.value = store.getShortLink;
            inputStyle.value = 'font-bold';
        });
    }

    const copyShortLink = () => {
        let textArea = document.createElement("textarea");
        textArea.value = link.value;
        textArea.style.position = "fixed";
        textArea.style.left = "-999999px";
        textArea.style.top = "-999999px";
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        return new Promise((res, rej) => {
            document.execCommand("copy") ? res() : rej();
            textArea.remove();

            // update button settings
            buttonSettings.message = 'Copied!';
            buttonSettings.style = 'bg-emerald-300 text-black';
            buttonSettings.onClick = () => {};
        });
    }

    return {
        buttonSettings,
        inputStyle,
    };
}