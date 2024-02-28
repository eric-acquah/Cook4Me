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
  controller('RegisterPageController', function($scope, RegisterService) {

    // $scope.registerAsOptions = 'client'

    $scope.optionTrigger = function(){
        if ($scope.registerAsOptions === 'cook'){
            $scope.registerAsCook = true;
            $scope.submitRegister.registeredAs = 'cook';
        } else {
            $scope.registerAsCook = false;
            $scope.reopenRegisterAs = false;
            $scope.submitRegister.registeredAs = 'client';
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

    // Toggles the submit and modal button
    $scope.notSubmitted = true;
    $scope.submitted = false;

    $scope.submitRegister = {};
    $scope.speciality = {};
    $scope.AuthDetails = {};

    collectAuth();

    /*###### HELPER FUNCTIONS START #######*/

    // Retrieve all auth data into sessionStorage
    function collectAuth(){

        let authDetails = [];

        if (sessionStorage.getItem('authDetails') == null){

            RegisterService.allAuth('logins').then(function(response){
                for (let obj in response){
                    authDetails.push(response[obj]);
                }
    
                sessionStorage.setItem('authDetails', angular.toJson(authDetails));
    
                console.log(sessionStorage.getItem('authDetails'));
            });
        }
    };
 
    // Check uniqueness of username
    function UsrNameIsUnique(usrname){
        let authStore = sessionStorage.getItem('authDetails');

        authStore = angular.fromJson(authStore); // convert back into array object

        for (let obj in authStore){
            if (authStore[obj].usrIdentity.usrName == usrname){
                return false;
            }
        }

        return true;
    }

    // Initializes speciality with the appropriate fields 
    function setSpeciality(){
        Object.keys($scope.domain).forEach(category => {
            $scope.speciality[category] = [];
        });
    }

    // Triggers 'is-invalid' classes
    function notValid(cls){

        angular.element(document.querySelectorAll(cls)).each(function(){
            const input = angular.element(this);
            if (input.hasClass('ng-invalid')){
                input.addClass('is-invalid');
            } else {
                input.removeClass('is-invalid');
            };
        });
    }

    function calculateAge(birthDate){
        const today = new Date();
        const fullBirthDate = new Date(birthDate);

        // calculate the age
        let age = today.getFullYear() - fullBirthDate.getFullYear()

        // adjust age if the birtday hasn't happened yet
        let monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0  || (monthDiff === 0 && today.getDate() < birthDate.getDate())){
            age--; 
        };

        return age;
    }

    function setDefaultPasswd(length = 8){
        const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        let password = "";

        for (let i = 0; i < length; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
        }

        return password;
    }

    function noValidation(){
        angular.element(document.querySelectorAll('.form-control, .form-select')).each(function(){
            const input = angular.element(this);
            if (input.hasClass('ng-invalid')){
                input.removeClass('is-invalid')
            } else {
                input.removeClass('is-invalid');
            };
        });
    }


    function dataSanitationFactory(){
        if ($scope.registerForm.$invalid && $scope.registerForm.$submitted){

            notValid('.form-control, .form-select');

            // sanitize cook's speciality data
            for (let key in $scope.speciality){
                list = [];
        
                list = Object.keys($scope.speciality[key]);

                if (!list.length){
                    $scope.isNotCheck = true;
                    // setSpeciality();
                    break;
                }
            };

        }
        
        // sanitize cook's speciality data
        for (let key in $scope.speciality){
            list = [];

            list = Object.keys($scope.speciality[key]);

            if (!list.length){
                $scope.isNotCheck = true;
                // setSpeciality();
                break;
            } else {
            $scope.isNotCheck = false;
            $scope.speciality[key] = list;
            };
        };

        console.log($scope.speciality);

        // Include the sanitized cook speciality object
        $scope.submitRegister.domain = {...$scope.speciality};

        // Set the address to location to match with API requirement
        $scope.submitRegister.location =  $scope.submitRegister.address

        // Get correct user age
        $scope.submitRegister.age = calculateAge($scope.submitRegister.birthDate);

        // Set default password for user
        $scope.submitRegister.password = setDefaultPasswd();
    }

    /*###### HELPER FUNCTIONS START ######*/


    setSpeciality(); // Initializes speciality object with the right fields. eg 'cuisine': [], 'dish': []


    // Submit form for creating new object via the API
    $scope.submitRegisterForm = function() {
        
        dataSanitationFactory(); // Sanitize data

        if ($scope.submitRegister.registeredAs === "cook"){
            
            const endpoint = "cooks";

            console.log($scope.submitRegister)

            RegisterService.registerCook(endpoint, $scope.submitRegister).then(function(response){
                console.log(response);

                $scope.AuthDetails.id = response.id
                $scope.AuthDetails.class = "cook";

                // Toggles the submit and modal button
                $scope.notSubmitted = false;
                $scope.submitted = true;

                $scope.$apply($scope.submitRegister = {}); // Clears form field after submission

                noValidation(); // Prevents validation after clearing form field

            });
            
        } else {
            const endpoint = "clients";

            console.log($scope.submitRegister)

            RegisterService.registerCook(endpoint, $scope.submitRegister).then(function(response){
                console.log(response);

                $scope.AuthDetails.id = response.id;
                $scope.AuthDetails.class = "client";

                 // Toggles the submit and modal button
                $scope.notSubmitted = false;
                $scope.submitted = true;

                $scope.$apply($scope.submitRegister = {}); // Clears form field after submission

                noValidation(); // Prevents validation after clearing form field
                
            });

        }
    }

    $scope.usrAuthDetails = function (){
        const endpoint = "logins"
        console.log($scope.AuthDetails);

        // Validate input before submission
        if ($scope.loginDetails.$invalid && $scope.loginDetails.$submitted){
            
            notValid('.form-control');
        }

        // check uniqueness of the username entered
        const isUnique = UsrNameIsUnique($scope.AuthDetails.usrName);

        if (isUnique == false){
            $scope.AuthDetails.usrName = ""; // Reset the name if it is not unique
        } else {

            // Making the values adhere to the endpoint rule
            $scope.AuthDetails.name = $scope.AuthDetails.usrName;
            $scope.AuthDetails.password = $scope.AuthDetails.usrPasswd;

            RegisterService.Auth(endpoint, $scope.AuthDetails).then(function(response){
                noValidation();
                // authDetails in sessionStorage is updated after each new submission
                sessionStorage.removeItem('authDetails');
                collectAuth();
                $('#registerModal').modal('hide');
                $scope.$apply($scope.AuthDetails = {});

                // Toggles the submit and modal button
                $scope.notSubmitted = true;
                $scope.submitted = false;
            });
            }       
    }

    $scope.discardModal = function(){
        noValidation();
        $scope.AuthDetails.usrName = "";
        $scope.AuthDetails.usrPasswd = "";
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