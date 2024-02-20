angular.module('liveApp.controllers', []).
  controller('HomePageController', function($scope, FlaskApiService) {
    $scope.appName = 'Cook4Me';
    $scope.nameFilter = null;
    $scope.driversList = [];
    $scope.allCooks = [];
    $scope.blankName = "Cook Name";
    $scope.totalClients = 20;
    $scope.defaultNum = 50;
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

    //If cooks objects are not loaded from database set default totalCooks value to 50
    if (!$scope.cook.length){
        $scope.totalCooks = 50;
    };

    $scope.totalCooks = $scope.cook.length;
        
    }
    );
    
  }).
  /* Service Controller */
  controller('ServicesPageController', function($scope, restAPIservice) {
   
  }).
  /* Login Controller */
  controller('LoginPageController', function($scope, restAPIservice) {
   
  }).
  /* Register Controller */
  controller('RegisterPageController', function($scope, restAPIservice) {
   
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