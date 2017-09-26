/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	config.extraPlugins= 'codesnippet';
	config.codeSnippet_theme = 'monokai_sublime';
	config.extraPlugins = 'uploadimage';
	config.extraPlugins = 'base64image';
	config.uploadUrl = '/media/static/blog/article_images/';

};
