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
        window.location.href='/toindex';
}
function gotoloadquery(){
        window.location.href='/load_query';
}
function gotoloadsummary(){
        window.location.href='/load_summary';
}
function gotoloaddelete(){
        window.location.href='/load_delete';
}
function gotoloadmodify(){
        window.location.href='/load_modify';
}