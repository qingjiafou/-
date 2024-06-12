function menu_active(ulId){
    if(ulId.style.display == "none"){
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
function goTofilePage() {
        window.location.href = '/file_upload';
    }
function gotoHome(){
        window.location.href = '/index';
}
function goToanalysePage(){
        window.location.href='/analyse_page';
}
function goTomodifyPage(){
        window.location.href='/modify_page/all';
}


