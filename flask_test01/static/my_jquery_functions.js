$(document).ready(function () {
    $("button").click(function () {
        $("#test").hide();
        $("ul li:first").css("background-color","blue");
        });
    $("#back").click(function () {
        $("#test").show();
        $("ul li:first").css("background-color","black");
    });
    $(".ex .hide").click(function () {
        $(this).parents(".ex").hide("slow");
    });
    $("button").click(function () {
        $("p").toggle("fast");
    });
    });
$(document).ready(function () {
   $("button").click(function () {
       $("#div1").fadeToggle();
       $("#div2").fadeToggle();
       $("#div3").fadeToggle();
   });
   $("#fadeout").click(function () {
       $("#div3").fadeOut(3000);
       $("#div2").fadeOut("slow");
       $("#div1").fadeOut();
   })
});
$(document).ready(function () {
   // $(".flip").click(function () {
   //     $(".panel").slideDown("slow");
   // });
   $(".flip").click(function () {
       $(".panel").slideToggle("slow");
   })
});

$(document).ready(function () {
    $("button").click(function () {
        $("div").animate({left:'250px',
        opacity:'0.5',
        height:'+=150px',
        width:'+=150px'});
    });
    $("button1").click(function () {
        $("div").animate({height:'toggle'
        });
    });
});

$(document).ready(function () {
    $("button").click(function () {
        $("#p1").css("color","red").slideUp(2000).slideDown(2000);
    });
});