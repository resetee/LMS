function query_role(){
	//删除表头下的行
	$("#row_table tr:gt(0)").remove();	
	var role_name = "超级管理员";
	var show_info = "<tr><td><input type='checkbox'></td><td>"
	+role_name+"</td><td><button class='see_right' onclick='see_right()'>查看权限</button></td><td><button class='set_right' onclick='set_right()'>分配权限</button><button class='delete_right' onclick='delete_right()'>删除</button></td></tr>";
	$("#row_table").append(show_info);
};

function see_right(){
	$(".see_right").each(
	function(){
		var role_name = $(this).parent().prev().text();
		console.log($(this))
		//根据角色名查找权限内容
		var right = role_name + "权限有:....";
		right1 = "<span>"+right+"</span>"
		$("#show_table_div").hide();
		$("#show_right_div").show();
		$("#show_right_div").append(right1)
		$("#show_right_div").click(function(){
			//情况显示框,隐藏显示框
			$("#show_right_div span").remove();
			$("#show_table_div").show();
			$("#show_right_div").hide();
		}); 
	}
	);
};

function set_right(){
	$(".see_right").each(
	function(){
		var role_name = $(this).prev().text();
		
		console.log(role_name)
	}
	
	);
};
