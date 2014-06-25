(function($) {
var seriesOptions = [],
yAxisOptions = [],
colors = Highcharts.getOptions().colors;

$.getJSON('http://176.56.238.64:8888/polistats', function(pdata) {				
		var keywords = ['Arvind Kejriwal', 'Narendra Modi', 'Rahul Gandhi', 'Sonia Gandhi', 'BJP', 'AAP', 'Congress India']
		var google_main_data = []
		var google_news_data = []

		for (var i = 0; i < keywords.length; ++i) {
			google_main_data.push({name: keywords[i], data: []});
			google_news_data.push({name: keywords[i], data: []});
		};

		for (var i = 0; i < pdata.length; ++i) {
				index_value = keywords.indexOf(pdata[i].name)
				google_main_data[index_value].data.push([pdata[i].time.$date, Math.log(pdata[i].google_main)]);
				google_news_data[index_value].data.push([pdata[i].time.$date, Math.log(pdata[i].google_news)]);
		}

		createChart('#container-gm', google_main_data, 'Google Main Search Trends');
		createChart('#container-gn', google_news_data, 'Google News Search Trends');
		
	});
function createChart(div_id, chart_data, text) {

	$(div_id).highcharts('StockChart', {

	    rangeSelector: {
			inputEnabled: $(div_id).width() > 480,
	        selected: 4
	    },

	    yAxis: {
	    	labels: {
	    		formatter: function() {
	    			return (this.value > 0 ? '+' : '') + this.value + '%';
	    		}
	    	},
	    	plotLines: [{
	    		value: 0,
	    		width: 2,
	    		color: 'silver'
	    	}]
	    },
	    
	    plotOptions: {
	    	series: {
	    		compare: 'percent'
	    	}
	    },
	    
	    tooltip: {
	    	pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
	    	valueDecimals: 2
	    },

	    title: {
				text: text
		},
	    
	    series: chart_data
	});
	
	}

})(jQuery);