'use strict';

angular.module("yunxuanyuCtrl", [])
    .controller('indexCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get("/static/api/all.json")
        .success(function(data, status, headers, config) {
            $scope.videoLists = data;
        });
    }])

    .controller('categoryCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get("/static/api/category.json")
        .success(function(data, status, headers, config) {
            $scope.categoryLists = data;
        });
    }])

    .controller("videoRankCtrl", ['$scope', '$http', function($scope, $http) {
        $http.get("/static/api/rank.json")
        .success(function(data, status, headers, config) {
            $scope.videoRankLists = data;
        });
    }])

    .controller("detailCtrl", ['$scope', '$http', function($scope, $http) {
        $http.get("/static/api/video.json")
        .success(function(data, status, headers, config) {
            $scope.video = data;
        });
    }])

    .controller("categoryListCtrl", ['$scope', '$http', function($scope, $http) {
        $http.get("/static/api/all.json")
        .success(function(data, status, headers, config) {
            $scope.videoLists = data;
        });
    }])
