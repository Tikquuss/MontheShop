<script src="{% static 'js/jquery/jquery-2.2.4.min.js' %}"></script>
var selectedImages = [];
function images_select(checkbox){
    a = checkbox.id.split('-')[1]
    if(checkbox.checked){
        selectedImages.push(a);
    }
    else{
        selectedImages.splice(selectedImages.indexOf(a));
        if(size(selectedImages)==0){
            //document.getElementById('button-submission').disable
        }
    }
    console.log(selectedImages);
}

function submission(){
    console.log(selectedImages);
    //*
    $.ajax({
        type: "POST",
        url: "validation",
        dataType: "json",
        traditional: true,
        data: {'list_article': JSON.stringify(selectedImages)},
        success: function(data) {
                console.log(data);
        },
        error:function(data) {
            console.log('error', data);
        }
    });
    //*/
    /*
    var r = new XMLHttpRequest(); 
    r.open("POST", "add_bouteille", true);
    
    r.onreadystatechange = function () {
        if (r.readyState != 4 || r.status != 200) return; 
        console.log(r.responseText);
    };
    
    r.send("d=d");
    */
}