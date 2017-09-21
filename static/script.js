$(window).scroll(function() {
var y_scroll_pos = window.pageYOffset;
var scroll_pos_test = 5;

if(y_scroll_pos > scroll_pos_test) {
   $("#top-strip").css("box-shadow","1px 1px 10px 1px #999");
}
else
{
  $("#top-strip").css("box-shadow","none"); 
}
});

document.getElementById('starter-input').addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode;
    if (key === 13) { // 13 is enter
        starter_input_tag = document.getElementById('starter-input');
        starter_input = starter_input_tag.value
        var ul = document.getElementById("starter-ul");
        var li1 = document.createElement("li");
        var li2 = document.createElement("li");
        li1.appendChild(document.createTextNode(starter_input));
        li2.appendChild(document.createTextNode(""));
        ul.appendChild(li1);
        ul.appendChild(li2);
        starter_input_tag.style.display = "none";
        ul.style.display = "block";
        document.getElementById("starter-title").style.display = "block";
        setCaret(li2)
    }
});

function setCaret(element) {
    var range = document.createRange();
    range.setStart(element.childNodes[0],0);
    range.collapse(true);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    return true;
}

Array.prototype.forEach.call(document.getElementsByClassName("shopping-list"), function(element){
  element.onmouseover = function(e){
    //make the controls visible on hover
    list_control_divs = element.getElementsByClassName("list-controls"); 
    Array.prototype.forEach.call(list_control_divs, function(element){
        element.style.visibility =  "visible";
    });
  };

    element.onmouseout = function(e){
    list_control_divs = element.getElementsByClassName("list-controls"); 
    Array.prototype.forEach.call(list_control_divs, function(element){
        element.style.visibility =  "hidden";
    });
  };
});
