$(function () {
    $(".uitem").hide();
    // $(".uitem").parent().on.("click", function () {
    //     $(this).show();
    // });
    // $(".litem > a").click(toggle(function (){
    //     $(this).next().slideDown();
    // },function () {
    //     $(this).next().slideUp();
    // }));
    $(".litem > a").click(function () {
        if($(this).next().hasClass("hidden")){
            $(this).next().show()
            $(this).next().removeClass("hidden");
        }else{
            $(this).next().hide();
            $(this).next().addClass("hidden");
        };
    });
});