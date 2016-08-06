Template.MainGame_2 = function (game) {
    
};
		var styleEffect= { font: "35px font_GDR", fill: "#fff34c", align: "center"};
		var styleResult = { font: "18px font_GDR", fill: "#e10020", align: "center"};
		

Template.MainGame_2.prototype = {

	create: function() {
		this.tween_time;
		this.cal_score = 0;

		this.speed_item = 200;
		this.speed_static = 350;
		this.speed_bg = 6;

		this.speed_game = 0.5;
		this.max_speed_game = 1.2;

		this.speed_player = 300;
		this.isGamestart = false;
		this.isGameover = false;
		this.timeGenerate = 0;
		this.timePlay = 30;
		this.currentTime = this.timePlay;
		this.timeItem = 5;
		this.items = [];
		this.stones = [];
		this.countItem = [];
		this.listItem = [];
		this.collect_text = [];
		this.groupItems = [];
		// this.groupWoods = [];
		this.groupStones = [];
		this.itemState = 0;
		this.groupItem;
		this.MAX_ITEM_PER_TYPE = 3;
		this.max_time_bar;
		// Sound

		// Game
		game.world.setBounds(0, -200, 460, 50000);
    	game.physics.startSystem(Phaser.Physics.ARCADE);
		game.physics.startSystem(Phaser.Physics.P2JS);
        game.physics.p2.setImpactEvents(true);
        game.physics.p2.restitution = 0.8;
        game.time.advancedTiming = true;
		game.forceSingleUpdate = true;
        this.cursors = game.input.keyboard.createCursorKeys();

        // Background
		this.background = this.add.tileSprite(0,0,460,1006, "bg_game");
		// Bounds
		var bounds = new Phaser.Rectangle(30, -200, 400, 960);
		customBounds = { left: null, right: null, top: null, bottom: null };
    	this.createPreviewBounds(bounds.x, bounds.y, bounds.width, bounds.height);

		// The player
		this.player = this.add.sprite(w/2, h-100, 'player');
		// this.player.body.enable = true;
		this.player.name = 'boy';
		this.player.anchor.setTo(0.5);
		this.player.smoothed = false;
	    this.player.animations.add('anim', [0,1,2,3], 5, true);
	    this.player.play('anim');

	    game.physics.p2.enable(this.player, false);
	    this.player.body.setCircle(this.player.width/3);
	    this.player.body.fixedRotation = true;
		
		// Item
		this.groupItem = game.add.group();
		this.groupItem.enableBody = true;
		this.groupItem.physicsBodyType = Phaser.Physics.P2JS;
		for(var i=0; i<data_item.length; i++){
			var pool = [];
			for(var j=0; j<this.MAX_ITEM_PER_TYPE; j++){
				var item = this.groupItem.create(-1000, -1000, 'item',i);
				item.anchor.setTo(0.5);
				item.body.setCircle(item.width/3);
				item.checkWorldBounds = true;
    			item.outOfBoundsKill = true;
    			item.body.fixedRotation = true;
				item.kill();
				pool.push(item);
			}
			this.groupItems.push(pool);
		}

		game.physics.p2.setPostBroadphaseCallback(this.checkVeg, this);

		// Obstacle stone
		this.groupStone = game.add.group();
		this.groupStone.enableBody = true;
		this.groupStone.physicsBodyType = Phaser.Physics.P2JS;
		for(var i=0; i<50; i++){
			var obstacle = this.groupStone.create(-500, -500, 'stone');
			obstacle.anchor.setTo(0.5);
			// obstacle.body.setCircle(obstacle.width/2,0,-50);
			obstacle.checkWorldBounds = true;
			obstacle.outOfBoundsKill = true;
			obstacle.body.static = true;
			obstacle.kill();
			this.groupStones.push(obstacle);
		}
	
	    //  The score
	    this.frame_score = game.add.sprite(w - 105, 10, 'score');
	    this.scoreText = game.add.text(w - 60, 30, this.cal_score, { font: "25px font_ND", fill: "#fff", align: "center"});	    
	    this.scoreText.anchor.setTo(0.5);

	    if(user_info != null){
	    	game.add.sprite(w - 97, 60, 'session');
		    var stringX = 'x'+user_info.total_play_session;
		    var xxx = game.add.text(w - 55, 82, stringX, { font: "20px font_ND", fill: "#fff", align: "center"});	    
			xxx.anchor.setTo(0.5);
	    }

	    // Collect Item
		for(var i=0; i<data_item.length; i++){
	    	this.countItem[i] =0;
	    	this.listItem[i] =0;

	    }


	    // Show bird
	    this.ShowBird();

	    // Start game
	    this.initGame();
		this.cal_score = 0;
		for(var i=0; i<15; i++) {
			if (data_item[i].score == 1) {
				var number = data_item[i].number;
				this.countItem[i] += number;
				this.listItem[i] += number;
				this.cal_score += data_item[i].score * number;
			}
			else{

			var number = data_item[i].number;
			this.countItem[i] += number;
			this.listItem[i] += number;
			this.cal_score += data_item[i].score * number;
		}
        //
        //
	    }

		if(this.isGameover) return;
		this.isGameover = true;
		this.ShowResult();
	},

	ShowBird : function(){
		this.bird = game.add.sprite(10, 300, 'bird');
		this.xxx = game.add.sprite(w/2 - 200,h/2+50, 'xxx');
		this.bird.visible = false;
		this.xxx.visible = false;
	},

	createPreviewBounds : function(x, y, w, h) {

	    var sim = game.physics.p2;

	    //  If you want to use your own collision group then set it here and un-comment the lines below
	    var mask = sim.boundsCollisionGroup.mask;

	    customBounds.left = new p2.Body({ mass: 0, position: [ sim.pxmi(x), sim.pxmi(y) ], angle: 1.5707963267948966 });
	    customBounds.left.addShape(new p2.Plane());
	    // customBounds.left.shapes[0].collisionGroup = mask;

	    customBounds.right = new p2.Body({ mass: 0, position: [ sim.pxmi(x + w), sim.pxmi(y) ], angle: -1.5707963267948966 });
	    customBounds.right.addShape(new p2.Plane());
	    // customBounds.right.shapes[0].collisionGroup = mask;

	    customBounds.top = new p2.Body({ mass: 0, position: [ sim.pxmi(x), sim.pxmi(y) ], angle: -3.141592653589793 });
	    customBounds.top.addShape(new p2.Plane());
	    // customBounds.top.shapes[0].collisionGroup = mask;

	    customBounds.bottom = new p2.Body({ mass: 0, position: [ sim.pxmi(x), sim.pxmi(y + h) ] });
	    customBounds.bottom.addShape(new p2.Plane());
	    // customBounds.bottom.shapes[0].collisionGroup = mask;

	    sim.world.addBody(customBounds.left);
	    sim.world.addBody(customBounds.right);
	    sim.world.addBody(customBounds.top);
	    sim.world.addBody(customBounds.bottom);

	},

	checkVeg : function(body1, body2) {
		if (body1.sprite.key == 'item' && body2.sprite.key == 'item'){
			return false;
		}
		if(body1.sprite.key == 'stone' || body2.sprite.key == 'stone'){
			return true;
		}
		// if(body1.sprite.key === 'wood' && body2.sprite.name === 'boy'){
		// 	this.CollisionWood(body1.sprite);
		// 	return true;
		// }
		// if(body2.sprite.key === 'wood' && body1.sprite.name === 'boy'){
		// 	this.CollisionWood(body2.sprite);
		// 	return true;
		// }
		if(body1.sprite.name != 'boy'){
			this.CollectItem(body1.sprite);
		}
		if(body2.sprite.name != 'boy'){
			this.CollectItem(body2.sprite);
		}
	    return true;
	},

	// CollisionWood : function(wood){
	// 	console.log('xxx');
	// 	wood.kill();
	// 	this.effectStar(wood.x+10, wood.y+50, false);
	// },

	update: function() {
		if(this.isGameover || !this.isGamestart){
			this.player.body.velocity.x = 0;
	    	this.player.body.velocity.y = 0;
			for(var i=0; i<this.items.length; i++)
	    		this.items[i].body.velocity.y = 0;
	    	return;
		} 
		if(this.player.y >= 800){
			this.bird.visible = true;
			this.xxx.visible = true;
		}else{
			this.bird.visible = false;
			this.xxx.visible = false;
		}

			this.background.tilePosition.y += this.speed_bg*this.speed_game;

			if (!game.device.desktop){
				if (game.physics.arcade.distanceToPointer(this.player, game.input.activePointer) > 8){
	    			game.physics.arcade.moveToPointer(this.player, this.speed_player);
	    		}
	    		else
			    {
			        // Otherwise turn off velocity because we're close enough to the pointer
			        this.player.body.velocity.x = 0;
		    		this.player.body.velocity.y = 0;
			    }
	    	}
	    	else{
		    	this.player.body.velocity.x = 0;
		    	this.player.body.velocity.y = 0;
			    if (this.cursors.left.isDown && this.player.x > 20)
			    {
			        this.player.body.velocity.x = -this.speed_player;
			    }
			    else if (this.cursors.right.isDown && this.player.x < w-20)
			    {
			        this.player.body.velocity.x = this.speed_player;
			    }

			    if (this.cursors.up.isDown)
			    {
			        this.player.body.velocity.y = -this.speed_player;
			    }
			    else if (this.cursors.down.isDown)
			    {
			        this.player.body.velocity.y = this.speed_player;
			    }	  

			    if(this.player.x > w)
			    	this.player.x = w;
			    else if(this.player.x < 0)
			    	this.player.x = 0
			    if(this.player.y > h)
			    	this.player.y = h;
			    else if(this.player.y < 0)
			    	this.player.y = 0;	    		
	    	}
	    	// Generate item
	        if (game.time.now > this.timeGenerate)
	        {
	            this.GenerateItem();
	        }	    	
	    	for(var i=0; i<this.items.length; i++){
	    		this.items[i].body.velocity.y = this.speed_item*this.speed_game;
	    		if(this.items[i].y >= 730){
	    			this.items[i].kill();
	    			// this.countItem[this.items[i]._frame.index]++;
	    		}
	    	}
	    	for(var i=0; i<this.stones.length; i++)
	    		this.stones[i].body.velocity.y = this.speed_static*this.speed_game;
	},

	updateTimeBar : function(time, type){
		game.tweens.remove(this.tween_time);
		if(type == 1){
			this.time_bar.width += (this.timeItem/this.timePlay)*this.max_time_bar;
		}else if(type == -1){
			this.time_bar.width -= (this.timeItem/this.timePlay)*this.max_time_bar;
		}else{
			this.time_bar.width = this.max_time_bar;
		}
        this.tween_time = this.game.add.tween(this.time_bar).to({ width: 0  }, time*1000, "Power1");
       	this.tween_time.onComplete.add(this.Gameover, this);
        this.tween_time.start();		
	},

	CollectItem : function(item){
		if(this.isGameover) return;
		sfx_eat.play();
		var textEffect;
		var isEffectStar = true;
		this.listItem[item._frame.index]++;
		this.cal_score += data_item[item._frame.index].score;
		switch(item._frame.index){
			case 0:
				this.effectScore(data_item[0].score, item.x-15, item.y-20,styleEffect);
				break;
			case 1:
				this.effectScore(data_item[1].score, item.x-15, item.y-20,styleEffect);
				break;
			case 2:
				this.effectScore(data_item[2].score, item.x-15, item.y-20,styleEffect);
				break;	
			case 3:
				this.effectScore(data_item[3].score, item.x-15, item.y-20,styleEffect);
				break;
			case 4:
				this.effectScore(data_item[4].score, item.x-15, item.y-20,styleEffect);
				break;	
			case 5:
				this.effectScore(data_item[5].score, item.x-15, item.y-20,styleEffect);
				break;
			case 6:
				this.effectScore(data_item[6].score, item.x-15, item.y-20,styleEffect);
				break;
			case 7:
				this.effectScore(data_item[7].score, item.x-15, item.y-20,styleEffect);
				break;	
			case 8:
				this.effectScore(data_item[8].score, item.x-15, item.y-20,styleEffect);
				break;
			case 9:		
				this.effectScore(data_item[9].score, item.x-15, item.y-20,styleEffect);
			case 10:
				this.effectScore(data_item[10].score, item.x-15, item.y-20,styleEffect);			
				break;
			case 11:
				this.effectScore(data_item[11].score, item.x-15, item.y-20,styleEffect);	
				break;	
			case 12:
				this.effectScore(data_item[12].score, item.x-15, item.y-20,styleEffect);			
				break;																	
			case 13:
				textEffect = "+"+this.timeItem+"s";
				this.effectScore(textEffect, item.x-15, item.y-20,styleEffect);
				this.currentTime += this.timeItem;
				if(this.currentTime > this.timePlay){
					this.currentTime = this.timePlay;
					this.updateTimeBar(this.currentTime,0);
				}else{
					this.updateTimeBar(this.currentTime,1);	
				}
				break;
			case 14:
				textEffect = "-"+this.timeItem+"s";
				this.effectScore(textEffect, item.x-15, item.y-20,styleEffect);
				this.currentTime -= this.timeItem;
				if(this.currentTime < 0){
					this.time_bar.width = 0;
					game.tweens.remove(this.tween_time);
					this.Gameover();
				}else{
					this.updateTimeBar(this.currentTime,-1);
				}
				isEffectStar = false;
				break;					
		}
		this.scoreText.text = this.cal_score;
		item.kill();
		this.effectStar(item.x+10, item.y+50, isEffectStar);
	},

	effectScore : function(value,x,y,style){
		var effect = game.add.text(x,y, value, style);
		var tween = game.add.tween(effect).to({y:y-50, alpha:0}, 600, "Linear", true);
	},

	updateCurrentTime: function (){
	    if(this.isGameover) {
	    	game.time.events.remove(this.timeLoop);
	    	return;
	    }
	    if(this.speed_game < this.max_speed_game)
	    	this.speed_game += 1/this.timePlay;
	    this.currentTime--;    
	},	

	Gameover : function(){

		if(this.isGameover) return;
		this.isGameover = true;
		this.ShowResult();
	},

	effectStar : function(x,y,isG){
		var effect;
		if(isG){
			effect = game.add.sprite(x,y,'effect_good');
		}else{
			effect = game.add.sprite(x,y,'effect_bad');
		}
		effect.anchor.setTo(0.5);
		effect.scale.setTo(0.5);
		game.add.tween(effect).to( { alpha: 0 }, 200, "Linear", true);
		game.add.tween(effect.scale).to( { x: 1, y:1 }, 200, "Linear", true);
	},

	ShowResult : function(){
		//
		game.add.sprite(0,0,'bg');
		var popup_tut = game.add.sprite(w/2, h/2, 'result_2');
		popup_tut.anchor.setTo(0.5, 0.5);
		var style = { font: "26px font_ND", align: "center"};

	    for(var i=0; i<10; i++){
	    	if(i<4){
	    		var text = game.add.text(w/2 -130 + 90*i, h/2 - 80, this.listItem[i]+' x '+data_item[i].score, styleResult);
	    		text.anchor.setTo(0.5, 0.5);
	    	}else if (i<8){
	    		var text = game.add.text(w/2 -130 + 90*(i-4), h/2 + 35, this.listItem[i]+' x '+data_item[i].score, styleResult);
	    		text.anchor.setTo(0.5, 0.5);
	    	}else{
	    		var text = game.add.text(w/2 -40 + 90*(i-8), h/2 + 150, '', styleResult);
	    		text.anchor.setTo(0.5, 0.5);
	    		if(i==8){
	    			var tmp = this.listItem[8] + this.listItem[9] + this.listItem[10] + this.listItem[11];
	    			text.text = tmp+' x '+data_item[8].score;
	    		}
	    		else{
	    			text.text = this.listItem[12]+' x '+data_item[12].score;
	    		}
	    	}
	    }
	    // this.cal_score = 0;
	    // for(var i=0; i<data_item.length; i++){
	    // 	this.cal_score += this.listItem[i]*data_item[i].score;
	    // }

		var scoreResultText = game.add.text(w/2+10, 580, this.cal_score,style);
		this.btn_continue = game.add.button(w/2, h-50, 'btn_continue', this.OnContinue, this);
	    this.btn_continue.anchor.setTo(0.5, 0.5);
	    state_animation = 0;
	    // this.btnAnimation();
	    
	},

	OnContinue : function(){
		sfx_click.play();
		SubmitScore(this.cal_score,2,this.listItem);
	},

	GenerateItem : function(){
		var tmp = 0;
		var tmp = game.rnd.integerInRange(0, 100);

			// Stone
			var ran;
			do{
				ran = game.rnd.integerInRange(0,13);



			}while(this.countItem[ran] >= data_item[ran].number);
			this.countItem[ran]++;
			var item = this.addItem(game.rnd.integerInRange(w/2 - 200, w/2 + 200), -30, ran, 1);
			if(item){
				this.items.push(item);
				if(this.items.length <= 1)
					this.itemAnimation();
			}
			tmp = game.rnd.integerInRange(300/this.speed_game, 600/this.speed_game);

		
		this.timeGenerate = game.time.now + tmp;
	},

	addItem: function(x, y,index, type) {
	  var item,
	    i = 0;
	  if (type === 1) {
	    for (i = 0; i < this.groupItems[index].length; i++) {
	      if (!this.groupItems[index][i].alive) {
	         item = this.groupItems[index][i];
	         item.reset(x, y);
	         return item;
	      }
	    }
	  }
	  return item;
	},

	// addWood: function(x, y, type) {
	//   var obstacle,
	//     i = 0;
	//   if (type === 1) {
	//     for (i = 0; i < this.groupWoods.length; i++) {
	//       if (!this.groupWoods[i].alive) {
	//          obstacle = this.groupWoods[i];
	//          obstacle.reset(x, y);
	//          return obstacle;
	//       }
	//     }
	//   }
	//   return obstacle;
	// },

	addStone: function(x, y, type) {
	  var obstacle,
	    i = 0;
	  if (type === 1) {
	    for (i = 0; i < this.groupStones.length; i++) {
	      if (!this.groupStones[i].alive) {
	         obstacle = this.groupStones[i];
	         obstacle.reset(x, y);
	         return obstacle;
	      }
	    }
	  }
	  return obstacle;
	},

	initGame : function(){
		this.isGamestart = true;
		this.isGameover = false;
		this.currentTime = this.timePlay;
		//  Time
	    this.timeLoop = game.time.events.loop(Phaser.Timer.SECOND, this.updateCurrentTime, this);
	    var time_base = game.add.sprite(w/2,h-23,'time_base');
	    time_base.anchor.setTo(0.5);
	    this.time_bar = game.add.sprite(0,h-32.5,'time_bar');
	    this.time_bar.x = w/2 - this.time_bar.width/2;
	    this.max_time_bar = this.time_bar.width;
	    this.updateTimeBar(this.timePlay,0);
	},

	itemAnimation : function(){
		if(this.items.length <= 0){
			return;
		}
		var newPosition = 0;
		var newScale = 0;
		var tween_0;
		if(this.itemState == 0){
			newPosition = 50;
			newScale = 0.1;
			this.itemState = 1;
		}else{
			newPosition = -50;
			newScale = -0.1;
			this.itemState = 0;
		}
		tween_0 = this.game.add.tween(this.items[0].scale).to({ x:  this.items[0].scale.x + newScale, y:  this.items[0].scale.y + newScale}, 1000, "Power1");
		tween_0.start();
		for(var i=1; i<this.items.length; i++){
			var tween_s = this.game.add.tween(this.items[i].scale).to({ x:  this.items[i].scale.x + newScale, y:  this.items[i].scale.y + newScale}, 1000, "Power1");
			tween_s.start();
		}
		tween_0.onComplete.add(this.itemAnimation, this);
	},

	btnAnimation : function(){
		var new_angle = 0;
		var time_move = 0;
		switch(state_animation){
			case 0:
				new_angle = 0;
				time_move = 0;
				state_animation ++;
				game.time.events.add(1500, this.btnAnimation, this);
				break;
			case 1:
				new_angle = 15;
				time_move = 100;
				state_animation ++;
				break;
			case 2:
				new_angle = -15;
				time_move = 200;
				state_animation ++;
				break;
			case 3:
				new_angle = 10;
				time_move = 100;
				state_animation ++;
				break;
			case 4:
				new_angle = -10;
				time_move = 70;
				state_animation ++;
				break;
			case 5:
				new_angle = 0;
				time_move = 50;
				state_animation = 0;
				break;				
		}
		if(state_animation != 1){
			var tween = this.game.add.tween(this.btn_continue).to({ angle: new_angle}, time_move, "Power1");
			tween.onComplete.add(this.btnAnimation, this);
			tween.start();	
		}
	},

	// render: function(){
 //        	game.debug.text('render FPS: ' + (game.time.fps || '--') , 2, 14, "#00ff00");

	// 		if (game.time.suggestedFps !== null)
	// 		{
	// 			game.debug.text('suggested FPS: ' + game.time.suggestedFps, 2, 28, "#00ff00");
	// 			game.debug.text('desired FPS: ' + game.time.desiredFps, 2, 42, "#00ff00");
	// 		}
 //    }
}
