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
        alert('📋 Content copied to clipboard: ' + textToCopy)
    } catch (err) {
        console.error('Failed to copy: ', err);
        alert('Failed to copy: ' + err)
    }
}

function handleClick(event) {
    const clickedElement = event.currentTarget;
    const isActive = clickedElement.classList.contains('active');
    const isMobile = window.matchMedia("(max-width: 480px)").matches;

    // Get the class names of the clicked element (excluding 'active' class)
    const classNames = Array.from(clickedElement.classList).filter(className => className !== 'active').join('.');

    // Remove elements with the same class (except 'active' class)
    var elements = document.querySelectorAll(`.${classNames}`);
    elements.forEach(function(el) {
        el.classList.remove('active');
    });

    // Add 'active' class to the clicked element
    clickedElement.classList.add('active');

    // Only copy to clipboard if it's not a mobile device or if it's a mobile device and the element is active
    if (!isMobile || (isMobile && isActive)) {
        copyToClipboard(event, 1);
    }
}

// Function to remove 'active' class from all elements with specific class except the clicked one
function removeActiveClass(event) {
    var elements = document.querySelectorAll('.tooltip.toleft');
    elements.forEach(function(el) {
        if (el !== event.target && !el.contains(event.target)) {
            el.classList.remove('active');
        }
    });
}

// Add event listener to document to remove 'active' class when clicking anywhere
document.addEventListener('click', function(event) {
    removeActiveClass(event);
});