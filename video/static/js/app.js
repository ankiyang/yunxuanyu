'use strict';

angular.module('yunxuanyu', [
    'ngRoute',
    'yunxuanyuCtrl',
    ])

    .config(["$interpolateProvider", "$routeProvider", function($interpolateProvider, $routeProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

        $routeProvider
            .when('/', {
                templateUrl: "/v/all",
                controller: 'indexCtrl',
            })

            .when('/:video_id', {
                templateUrl: "/v/detail/",
                controller: 'detailCtrl',
            })

            .when('/c/:category', {
                templateUrl: '/v/category/',
                controller: 'categoryListCtrl',
            })

            .otherwise('/')
    }])