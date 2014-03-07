$(function() {
   $(".datepicker").datepicker({ dateFormat: 'yy-mm-dd' });
});

$(document).ready(function(){
	
	$( ".datepicker" ).click(function() {
  		translateMonthDays();
	});
	
	$(document).on("click",".ui-datepicker-next", function() {
  		translateMonthDays();
	});
	
	$(document).on("click",".ui-datepicker-prev", function() {
  		translateMonthDays();
	});
	
});


function translateMonthDays(){
		var currentmonth = $( ".ui-datepicker-month" ).html();
  		var url = window.location.href.toString();
  		var isGeorgian = (url.indexOf("/ka/") != -1);
  		if (isGeorgian){
  			// Translating months
  			var translatedMonth = getGeorgianMonth(currentmonth);
  			$( ".ui-datepicker-month" ).html(translatedMonth);
  			
  			// Translating days
  			translateDays();
  			
  			// Translating "Prev" and "Next" title attributes, on left and right arrows.
  			$(".ui-datepicker-prev").prop('title','წინა');
  			$(".ui-datepicker-next").prop('title','შემდეგ');
  			
  		}
	}
	
	function translateDays(){
		$('.ui-datepicker-calendar > thead  > tr > th').each(function() {
			var thisSpan = $(this).find('span');
	        var translatedDay = getGeorgianDay(thisSpan.text());
	        var shortTranslatedDay = translatedDay.substring(0,2);
	        thisSpan.prop('title',translatedDay);
	        thisSpan.text(shortTranslatedDay);
		});
	}
	
	
	function getGeorgianMonth(currentMonth){
		var result = "";
		if (currentMonth == "January"){
			result = "იანვარი";
		} else if (currentMonth == "February"){
			result = "თებერვალი";
		} else if (currentMonth == "March"){
			result = "მარტი";
		} else if (currentMonth == "April"){
			result = "აპრილი";
		} else if (currentMonth == "May"){
			result = "მაისი";
		} else if (currentMonth == "June"){
			result = "ივნისი";
		} else if (currentMonth == "July"){
			result = "ივლისი";
		} else if (currentMonth == "August"){
			result = "აგვისტო";
		} else if (currentMonth == "September"){
			result = "სექტემბერი";
		} else if (currentMonth == "October"){
			result = "ოქტომბერი";
		} else if (currentMonth == "November"){
			result = "ნოემბერი";
		} else if (currentMonth == "December"){
			result = "დეკემბერი";
		} 
		return result;
	}
	
	function getGeorgianDay(currentDay){
		var result = "";
		if (currentDay == "Mo"){
			result = "ორშაბათი";
		} else if (currentDay == "Tu"){
			result = "სამშაბათი";
		} else if (currentDay == "We"){
			result = "ოთხშაბათი";
		} else if (currentDay == "Th"){
			result = "ხუთშაბათი";
		} else if (currentDay == "Fr"){
			result = "პარასკევი";
		} else if (currentDay == "Sa"){
			result = "შაბათი";
		} else if (currentDay == "Su"){
			result = "კვირა";
		}
		return result;
	}