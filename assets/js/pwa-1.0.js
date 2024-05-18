---
layout: null 
---
window.onload = function () {
    var script = document.createElement('script');
    var firstScript = document.getElementsByTagName('script')[0];
    script.async = true;
    script.src = '{{'sw-register.js'|relative_url}}?v=' + Date.now();
    firstScript.parentNode.insertBefore(script, firstScript);
};
window.addEventListener("sw.update", function() {
    alert("The site has been updated with new content. The page will now reload to apply these updates.");
    window.location.reload(true);
});