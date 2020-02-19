var selectedImages = [];
var pannier_vide = 'Pennier vide';
var sauvegarder = 'Sauvegarder';
var span = document.getElementById("button-submission");
var permanent_modal = document.getElementById("pattern-switcher")
//*
permanent_modal.disabled = true;
for(checkbox of document.getElementsByTagName('checkbox')){
    if(checkbox.checked){
        permanent_modal.disabled = false;
        span.innerText = sauvegarder;
        //permanent_modal.setAttribute('style', 'background-color : greed');
        break;
    }   
    span.innerText = pannier_vide;   
}
//*/
/*
$(document).ready(function(){
    permanent_modal.disabled = true;
    for(checkbox of document.getElementsByTagName('checkbox')){
        if(checkbox.checked){
            permanent_modal.disabled = false;
            span.innerText = sauvegarder;
            //permanent_modal.setAttribute('style', 'background-color : greed');
            break;
        }   
        span.innerText = pannier_vide;   
    }
});
*/
function images_select(checkbox){
    a = checkbox.id.split('-')[1]
    if(checkbox.checked){
        selectedImages.push(a);
    }
    else{
        selectedImages.splice(selectedImages.indexOf(a));
    }
    console.log(selectedImages);

    if(selectedImages.length != 0){
        permanent_modal.disabled = false;
        span.innerText =  sauvegarder;
    }else{
        span.innerText = pannier_vide;
        permanent_modal.disabled = true;
    }
}

function submission(){
    console.log(selectedImages);
    //window.location.reload(true);
    //window.location.replace('http://127.0.0.1:8000/log')
    //window.location.assign('http://127.0.0.1:8000/log');
    flag = false
    console.log('Flag = ', flag);
    if (selectedImages.length != 0 ){
        $.ajax({
            type: "GET",
            url: "validation",
            dataType: "json",
            traditional: true,
            data: {'list_article': JSON.stringify(selectedImages)},
            success: function(data) {
                    console.log(data);
                    flag = true;
            },
            error:function(data) {
                console.log('error', data);
            }
        });
    }
    // Le backend n'a pas récu la demande
    if(!flag){
        //location.href = '/';
        //*
        $.ajax({
            type: "POST",
            url: "error",
            dataType: "json",
            traditional: true,
            data: {'origin': JSON.stringify(selectedImages),
                    'message' : JSON.stringify('rechargez la page')},
            success: function(data) {
                    console.log("error", data);
            },
            error:function(data) {
                console.log('error 1', data);
            }
        });
        //*/
    }
}

function modifier(){
    console.log('modifier');
    document.getElementById('username').disabled = false;
    document.getElementById('password').disabled = false;
    document.getElementById('modal-link').disabled = true;
}