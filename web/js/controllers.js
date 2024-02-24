angular.module('liveApp.controllers', []).
  controller('HomePageController', function($scope, FlaskApiService, ReviewsAccess, $rootScope) {
    $scope.appName = 'Cook4Me';
    $scope.nameFilter = null;
    $scope.driversList = [];
    $scope.allCooks = [];
    $scope.blankName = "Cook Name";
    $scope.totalClients = 20;
    $scope.defaultNum = 50;
    $scope.inputPlaceholder = "I really love this app!";
    $scope.namePlaceholder = "Client Name";
    $scope.emailPlaceholder = "Email";

    let cooks_endpoint = "cooks";

    FlaskApiService.getData(cooks_endpoint).then(function(response){
        for (let data in response){
            $scope.allCooks.push(response[data]);

        }   
        
    // If there are no objects retrived from the database set 8 dummy values to display in the view
    $scope.cook = [];

    // Loops over each cook object in allCooks and creates a more flexible object for each 
    for (let obj in $scope.allCooks){

        keep = {}; // create a new object through each iteration

        for (let key in $scope.allCooks[obj]){

            if (key == "_UserBase__user_credentials"){
                keep.name = $scope.allCooks[obj][key].UserName;
                keep.id = $scope.allCooks[obj][key].UserId;
                keep.passwd = $scope.allCooks[obj][key].UserPasswd;

            } else {
                keep[key] = $scope.allCooks[obj][key]
            }
        }
        $scope.cook.push(keep)          
    }

    //Sets the totalCooks value to be displayed in the view
    $scope.totalCooks = $scope.cook.length;    
    }

    );

    // Display reviews
    ReviewsAccess.getReview().then(function(reviewStore){
        $scope.allReviews = reviewStore;
    });

    // listen and Hot-reaload after each form submission
    $scope.$on('reviewAdded', function(event, newReview){
 
        $scope.allReviews.push(newReview);
        $scope.$apply($scope.allReviews) // Force re-rendering of objects. #!Not the best approach tho#!
        $scope.feedbackReact = "Thanks for your feedback";

    // clear the feedbackReact upon a scroll
    $scope.clearReact = function(){
        $scope.$apply($scope.feedbackReact = "");
     }

    });

    
  }).
  controller('feedbackCtrl', function($scope, ReviewsAccess, $rootScope){

    $scope.UserFeedback = {};

    $scope.submitFeedback = function () {
        ReviewsAccess.addReview($scope.UserFeedback).then(function(createdReview){
            // Broadcast each new submission for view controller to reload
            $scope.newReview = createdReview;
            $rootScope.$broadcast('reviewAdded', $scope.newReview);
            $scope.$apply($scope.UserFeedback = {}) // Reset the model to clear form field

            $scope.feedbackForm.$setPristine();
            $scope.feedbackForm.$setUntouched();
        });
    };

  }).
  /* Service Controller */
  controller('ServicesPageController', function($scope, restAPIservice) {
   
  }).
  /* Login Controller */
  controller('LoginPageController', function($scope, restAPIservice) {
   
  }).
  /* Register Controller */
  controller('RegisterPageController', function($scope, FlaskApiService) {

    // $scope.registerAsOptions = 'client'

    $scope.optionTrigger = function(){
        if ($scope.registerAsOptions === 'cook'){
            $scope.registerAsCook = true;
        } else {
            $scope.registerAsCook = false;
            $scope.reopenRegisterAs = false;
        }
    }

    $scope.closeField = function(){
        $scope.registerAsCook = false;
        $scope.reopenRegisterAs = true; // Toggle to reopen registerAsCook
    }

    $scope.ReopenRegisterAs = function(){
        $scope.registerAsCook = true;
        $scope.reopenRegisterAs = false; // disappears after reopening registerAsCook
    }

    // Speciality object 
    $scope.domain = {
        'cuisine': ["global", "regional", "dietary"],
        'dish': ["appetizers_and_snacks", "main_courses", "sides_and_soups", "desserts", "baking"],
        'cooking_style': ["classic", "modern", "healthy", "street_food"]
      };

    // Let the Bio field show by default
    $scope.toggle = "Next";
    $scope.label = "Bio"
    $scope.toBio = true;

    // Toggles between the Bio field and the Speciality field
    $scope.switcField = function (){

        if ($scope.toggle !== "Previous"){
            // Toggle to speciality field
            $scope.label = "Speciality"
            $scope.toBio = false;
            $scope.toDomain = true;

            $scope.toggle = "Previous"; // Changes the button text to "Previous"
        } else {
            // Toggle to Bio field
            $scope.label = "Bio";
            $scope.toDomain = false;
            $scope.toBio = true;

            $scope.toggle = "Next"; // Changes the button text to "Next"
        };
    }
  }).
  /* About Controller */
  controller('AboutPageController', function($scope, restAPIservice) {
   
  }).
  /* Feed Controller */
  controller('FeedPageController', function($scope, restAPIservice) {
   
  }).
  /* Contact Controller */
  controller('ContactPageController', function($scope, restAPIservice) {
  }
  );


  restAPIservice.appInit().then(function() {
    const token = sessionStorage.getItem('_token');
    if(!token){
        $scope.initApp();
    }
})


/*Referance code. Thanks to @Rsgyan*/
// $scope.initApp = function(){
//     var action = 'initapp';
//     restAPIservice.getData(action).then(function(response) {
//         if(response.data.msg === 'success'){
//             const repo = response.data.data;
//             sessionStorage.setItem('_token',repo.token);
//             sessionStorage.setItem('_id',repo.id);
//             sessionStorage.setItem('_cipher',repo.cipher);
//             sessionStorage.setItem('_payment',repo.payment);
//             sessionStorage.setItem('_company',repo.company);
//             sessionStorage.setItem('_img_url',repo.imgurl);
//         }else{
//             console.log('Error loading data: ',response.data.data);
//         }
//     });
// }