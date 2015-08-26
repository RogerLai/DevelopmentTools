jQuery(document).ready(function () {
	jQuery("#redeploy_btn").click(function(){	
		jQuery.ajax({
			type: "get",
			url: "/redeploy",
			success: function (data) {
				jQuery("#deploy_result").html(data);
			},
			error: function () {
				alert("请求失败，请稍后重试");
			}
		});
	});
})