﻿(function($) {
	'use strict';
	jQuery('.mean-menu').meanmenu({
		meanScreenWidth: "991"
	});
	$(window).on('scroll', function() {
		if ($(this).scrollTop() > 150) {
			$('.navbar-area').addClass("sticky-nav");
		} else {
			$('.navbar-area').removeClass("sticky-nav");
		}
	});
	$(".burger-menu").on('click', function() {
		$('.sidebar-modal').toggleClass('active');
	});
	$(".sidebar-modal-close-btn").on('click', function() {
		$('.sidebar-modal').removeClass('active');
	});
	$(".side-nav-responsive .dot-menu").on("click", function() {
		$(".side-nav-responsive .container .container").toggleClass("active");
	});
	$('.services-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		dots: false,
		autoplay: true,
		rtl: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
		navText: ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"],
	})
	$('.room-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: false,
		dots: true,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
	})
	$('.show-comment-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		dots: false,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
		navText: ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"],
	})
	$('.show-comment-slider-two').owlCarousel({
		loop: true,
		items: 1,
		margin: 30,
		rtl: true,
		nav: false,
		dots: true,
		autoplay: true,
		autoplayHoverPause: true,
	})
	$('.show-comment-slider-three').owlCarousel({
		loop: true,
		margin: 30,
		nav: false,
		dots: true,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
	})
	$('.show-comment-slider-area').owlCarousel({
		loop: true,
		items: 1,
		margin: 30,
		nav: false,
		dots: true,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
	})
	$('.team-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		dots: false,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
		navText: ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"],
	})
	$('.team-slider-two').owlCarousel({
		loop: true,
		margin: 30,
		nav: false,
		dots: true,
		rtl: true,
		autoplay: true,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			},
			768: {
				items: 2
			},
			1000: {
				items: 3
			}
		},
	})
	$('.room-details-slider').owlCarousel({
		loop: true,
		margin: 30,
		items: 1,
		nav: true,
		rtl: true,
		dots: false,
		autoplay: true,
		autoplayHoverPause: true,
		navText: ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"],
	})
	$('.gallery-view').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0, 1]
		}
	});
	$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
	$('.tab ul.tabs li a').on('click', function(g) {
		var tab = $(this).closest('.tab'),
			index = $(this).closest('li').index();
		tab.find('ul.tabs > li').removeClass('current');
		$(this).closest('li').addClass('current');
		tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
		tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
		g.preventDefault();
	});
	$('.accordion').find('.accordion-title').on('click', function() {
		$(this).toggleClass('active');
		$(this).next().slideToggle('fast');
		$('.accordion-content').not($(this).next()).slideUp('fast');
		$('.accordion-title').not($(this)).removeClass('active');
	});
	$('#datetimepicker').datepicker({
		rtl: true
	});
	$('#datetimepicker-check').datepicker({
		rtl: true
	});
	new WOW().init();
	$('select').niceSelect();
	$('body').append('<div id="toTop" class="top-btn"><i class="bx bx-chevrons-up"></i></div>');
	$(window).on('scroll', function() {
		if ($(this).scrollTop() != 0) {
			$('#toTop').fadeIn();
		} else {
			$('#toTop').fadeOut();
		}
	});
	$('#toTop').on('click', function() {
		$("html, body").animate({
			scrollTop: 0
		}, 1000);
		return false;
	});

	function makeTimer() {
		var endTime = new Date("October 30, 2021 17:00:00 PDT");
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400);
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") {
			hours = "0" + hours;
		}
		if (minutes < "10") {
			minutes = "0" + minutes;
		}
		if (seconds < "10") {
			seconds = "0" + seconds;
		}
		$("#days").html(days + "<span>روز</span>");
		$("#hours").html(hours + "<span>ساعت</span>");
		$("#minutes").html(minutes + "<span>دقیقه</span>");
		$("#seconds").html(seconds + "<span>ثانیه</span>");
	}
	setInterval(function() {
		makeTimer();
	}, 300);
	$(".newsletter-form").validator().on("submit", function(event) {
		if (event.isDefaultPrevented()) {
			formErrorSub();
			submitMSGSub(false, "لطفا ایمیل خود را به درستی وارد کنید.");
		} else {
			event.preventDefault();
		}
	});

	function callbackFunction(resp) {
		if (resp.result === "success") {
			formSuccessSub();
		} else {
			formErrorSub();
		}
	}

	function formSuccessSub() {
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "از اشتراک شما متشکریم!");
		setTimeout(function() {
			$("#validator-newsletter").addClass('hide');
		}, 4000)
	}

	function formErrorSub() {
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
			$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}

	function submitMSGSub(valid, msg) {
		if (valid) {
			var msgClasses = "validation-success";
		} else {
			var msgClasses = "validation-danger";
		}
		$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
	}
	$(".newsletter-form").ajaxChimp({
		url: "https://envyTheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9",
		callback: callbackFunction
	});
	jQuery(window).on('load', function() {
		jQuery(".preloader").fadeOut(500);
	});
})(jQuery);