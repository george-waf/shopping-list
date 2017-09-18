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