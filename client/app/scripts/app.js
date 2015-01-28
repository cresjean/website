'use strict';

/**
 * @ngdoc overview
 * @name crespowangSiteApp
 * @description
 * # crespowangSiteApp
 *
 * Main module of the application.
 */
angular
  .module('crespowangSiteApp', [
    'ngResource',
    'ngAnimate',
    'ngRoute',
    'ngTouch',
    'timer'


  ])
  .config(function ($routeProvider, $injector) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        resolve: $injector.get('MyStatResolveMap')
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
