'use strict';

angular.module('yunxuanyu', [
    'ngRoute',
    ])

    .config(["$interpolateProvider", "$routeProvider", function($interpolateProvider, $routeProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

        $routeProvider
            .when('/', {
                templateUrl: "/v/list",
            })

            .when('/:video_id', {
                templateUrl: "/v/detail/"
            })
    }])