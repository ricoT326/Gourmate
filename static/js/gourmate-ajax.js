$(document).ready(function(){
	$('#like_btn_recipe').click(function(){
		var recipeIdVar;
		recipeIdVar = $(this).attr('data-recipeid');

		$.get('/gourmate/like_recipe/',
		    {'recipe_id': recipeIdVar},
		    function(data){
			    $('#like_count_recipe').html(data);
			    $('#like_btn_recipe').hide();
		    })
	});
	
	$('#like_btn_comment').click(function(){
		var commentIdVar;
		commentIdVar = $(this).attr('data-commentid');

		$.get('/gourmate/like_comment/',
		    {'comment_id': commentIdVar},
		    function(data){
			    $('#like_count_comment').html(data);
			    $('#like_btn_comment').hide();
		    })
	});
});