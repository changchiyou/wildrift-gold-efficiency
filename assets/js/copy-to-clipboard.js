function copyToClipboard(event, deep = 0) {
    const element = event.currentTarget;

    let textToCopy = '';

    function getTextFromElement(element, depth) {
        if (depth === 0) {
            textToCopy += element.innerText || element.textContent;
        } else {
            const children = element.children;
            for (let i = 0; i < children.length; i++) {
                getTextFromElement(children[i], depth - 1);
            }
        }
    }

    getTextFromElement(element, deep);

    try {
        navigator.clipboard.writeText(textToCopy);
        console.log('Content copied to clipboard: ', textToCopy);
        alert('Content copied to clipboard: ' + textToCopy)
    } catch (err) {
        console.error('Failed to copy: ', err);
        alert('Failed to copy: ' + err)
    }
}