var url = "/t/"
var tag = new Array("#lightRedState", "#lightGreenState", "#lightBlueState", "#lightPurpleState","#lightRedDegree", "#lightGreenDegree", "#lightBlueDegree", "#lightPurpleDegree", "#diviceAerofluxus", "#diviceAirConditioning", "#diviceWaterPump1", "#diviceWaterPump2")
var divice_name = new Array("lightRedState", "lightGreenState", "lightBlueState", "lightPurpleState","lightRedDegree", "lightGreenDegree", "lightBlueDegree", "lightPurpleDegree", "diviceAerofluxus", "diviceAirConditioning", "diviceWaterPump1", "diviceWaterPump2")
//var divice_state = new Array("off", "off", "off", "off", 0, 0, 0, 0, "off", "off", "off","off");

// 红光开关
$(tag[0]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  1, diviceType: 0, diviceState: state}, function(){
				alert(divice_name[0]+"ok");
			});
		});

// 绿光开关
$(tag[1]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
//			if state:
//			    state = 1;
//			else:
//			    state = 0 ;
			$.get(url, {diviceNum:  2, diviceType: 0, diviceState: state}, function(){
				alert(divice_name[1]+"ok");
			});
		});

// 蓝光开关
$(tag[2]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  3, diviceType: 0, diviceState: state}, function(){
				alert(divice_name[2]+"ok");
			});
		});

// 紫光开关
$(tag[3]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  4, diviceType: 0, diviceState: state}, function(){
				alert(divice_name[3]+"ok");
			});
		});

// 红光强度
$(tag[4]).change(function(){
			// console.log($("#red").val());
			$.get(url, {diviceNum: 4, diviceState: $(tag[4]).val()}, function(){
				alert(divice_name[4]+"ok");
			});
		});

// 绿光强度
$(tag[5]).change(function(){
			// console.log($("#red").val());
			$.get(url, {diviceNum: 5,diviceState: $(tag[5]).val()}, function(){
				alert(divice_name[5]+"ok");
			});
		});

// 蓝光强度
$(tag[6]).change(function(){
			// console.log($("#red").val());
			$.get(url, {diviceNum: 6,diviceState: $(tag[6]).val()}, function(){
				alert(divice_name[6]+"ok");
			});
		});

// 紫光强度
$(tag[7]).change(function(){
			// console.log($("#red").val());
			$.get(url, {diviceNum: 7,diviceState: $(tag[7]).val()}, function(){
				alert(divice_name[7]+"ok");
			});
		});

// 排气开关
$(tag[8]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  8, diviceState: state}, function(){
				alert(divice_name[8]+"ok");
			});
		});

// 空调开关
$(tag[9]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  9, diviceState: state}, function(){
				alert(divice_name[9]+"ok");
			});
		});


// 水泵开关
$(tag[10]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  10, diviceState: state}, function(){
				alert(divice_name[10]+"ok");
			});
		});

// 紫光开关
$(tag[11]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {diviceNum:  11, diviceState: state}, function(){
				alert(divice_name[11]+"ok");
			});
		});