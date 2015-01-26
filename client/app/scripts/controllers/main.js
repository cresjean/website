'use strict';

/**
 * @ngdoc function
 * @name crespowangSiteApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the crespowangSiteApp
 */
angular.module('crespowangSiteApp')
  .controller('MainCtrl', function ($scope, $log, $resource, mystat) {
    $scope.stat = mystat;
    var waypoint = new Waypoint({
        offset: '70%',
        triggerOnce: true,
        element:  document.getElementById('stats'),
        handler: function(direction) {
            $('.timer').each(function() {
                var source_key = $(this).data('source');
                $(this).delay(6000).countTo({
                    from: 0,
                    to: mystat[source_key],
                    speed: 3000,
                    refreshInterval: 50
                });
        });
        }
    });
  })
  .constant("MyStatResolveMap", {
    mystat: function(Stats){
        return Stats.get_code_stat();

    }
    })
  .factory('Stats', function($resource){
        return {
            get_code_stat: function(){
                var resource = $resource('/api/code');
                return resource.get().$promise;
            }

        }
    });
;
