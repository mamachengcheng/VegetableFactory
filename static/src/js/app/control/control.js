var url = "/controlAPIView/"
var tag = new Array("#lightRedState", "#lightGreenState", "#lightBlueState", "#lightPurpleState","#lightRedDegree", "#lightGreenDegree", "#lightBlueDegree", "#lightPurpleDegree", "#diviceAerofluxus", "#diviceAirConditioning", "#diviceWaterPump1", "#diviceWaterPump2")
var divice_name = new Array("lightRedState", "lightGreenState", "lightBlueState", "lightPurpleState","lightRedDegree", "lightGreenDegree", "lightBlueDegree", "lightPurpleDegree", "diviceAerofluxus", "diviceAirConditioning", "diviceWaterPump1", "diviceWaterPump2")

// 红光开关
$(tag[0]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
//			alert(state)
			$.get(url, {"diviceNum":  1, "controlType": 0, "diviceState": state}, function(data){
			});
		});

// 绿光开关
$(tag[1]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  2, "controlType": 0, "diviceState": state}, function(){
			});
		});

// 蓝光开关
$(tag[2]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  3, "controlType": 0, "diviceState": state}, function(){
			});
		});

// 紫光开关
$(tag[3]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  4, "controlType": 0, "diviceState": state}, function(){
			});
		});

// 红光强度
$(tag[4]).change(function(){
			// console.log($("#red").val());
			$.get(url, {"diviceNum": 5, "controlType": 1, "diviceState": $(tag[4]).val()}, function(){
			});
		});

// 绿光强度
$(tag[5]).change(function(){
			// console.log($("#red").val());
			$.get(url, {"diviceNum": 6, "controlType": 1, "diviceState": $(tag[5]).val()}, function(){
			});
		});

// 蓝光强度
$(tag[6]).change(function(){
			// console.log($("#red").val());
			$.get(url, {"diviceNum": 7, "controlType": 1, "diviceState": $(tag[6]).val()}, function(){
				alert(data);
			});
		});

// 紫光强度
$(tag[7]).change(function(){
			// console.log($("#red").val());
			$.get(url, {"diviceNum": 8, "controlType": 1, "diviceState": $(tag[7]).val()}, function(){
				alert(data);
			});
		});

// 排气开关
$(tag[8]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  8, "controlType": 0, "diviceState": state}, function(){
				alert(data);
			});
		});

// 空调开关
$(tag[9]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  9, "controlType": 0, "diviceState": state}, function(){
				alert(data);
			});
		});


// 水泵开关
$(tag[10]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  10, "controlType": 0, "diviceState": state}, function(){
				alert(data);
			});
		});

// 水泵2开关
$(tag[11]).on('switchChange.bootstrapSwitch', function(event, state) {
			console.log(state);
			$.get(url, {"diviceNum":  11, "controlType": 0, "diviceState": state}, function(){
				alert(divice_name[11]+"ok");
			});
		});

//$.ajax({
//    url:"/ajaxAPIView/",
//    data:{val: $("#ajax_input").val()},
//    method: "get",
//    success: function(data){
//       $("#ajax").append(data);
//    }
//   })



//function get_data()
//{
//    $.ajax({
//        url:"/ajaxAPIView/",
//        data:{val: $("#ajax_input").val()},
//        method: "get",
//        success: function(data){
//           $("#ajax").append(data);
//        }
//       })
//}
//
//setInterval("get_data()",3000);//3秒一次执行



