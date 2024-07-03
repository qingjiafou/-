function menu_active(ulId) {
    if (ulId.style.display == "none") {
        ulId.style.display = "block";
    } else {
        ulId.style.display = "none";
    }
}

function changeCursor(element) {
    element.classList.add('cursor-pointer');
}

function resetCursor(element) {
    element.classList.remove('cursor-pointer');
}

function gotoHome() {
    var url = document.getElementById("homeButton").getAttribute("data-url");
    window.location.href = url;
}

function goTofilePage() {
    var url = document.getElementById("filePageButton").getAttribute("data-url");
    window.location.href = url;
}

function goToanalysePage() {
    var url = document.getElementById("analysePageButton").getAttribute("data-url");
    window.location.href = url;
}

function goTomodifyPage() {
    var url = document.getElementById("modifyPageButton").getAttribute("data-url");
    window.location.href = url;
}


