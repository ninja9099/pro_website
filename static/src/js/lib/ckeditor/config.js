/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	config.uiColor = '#AADC6E';
	// config.extraPlugins = 'codemirror';
	config.extraPlugins= 'codesnippet';
	config.extraPlugins = 'autogrow';
	config.codeSnippet_theme = 'monokai_sublime';
	// config.extraPlugins = 'imageuploader';
	config.extraPlugins = 'uploadimage';
	config.extraPlugins = 'base64image';
	config.uploadUrl = '/media/static/blog/article_images/';

};
