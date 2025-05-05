const mix = require( 'laravel-mix' );
const path = require( 'path' );
const publicPath = path.normalize( `static` );

// Require the eslint webpack plugin.
const ESLintPlugin = require( 'eslint-webpack-plugin' );

// Sets the relative path of the folder we build to.
mix.setPublicPath( publicPath );

const sassConfig = {
	processCssUrls: false,
};

const stylelintConfig = {
	configFile: '.stylelintrc',
	context: 'src/sass',
	failOnError: false,
	failOnWarning: false,
	quiet: false,
	fix: true,
};

// Custom webpack configuration.
mix.webpackConfig( {
	// Externals - Load React and ReactDOM so we can use react dependent npm packages.
	resolve: {
		alias: {
		  react: path.resolve('./node_modules/react'),
		  'react-dom': path.resolve('./node_modules/react-dom'),
		},
		extensions: [ '.js', '.jsx' ]
	},
	externals: {
	},
	plugins: [
		// Lint our JS files and attempt to fix issues automatically.
		new ESLintPlugin( {
			context: './src/js/',
			fix: mix.inProduction(),
			overrideConfigFile: path.resolve( __dirname, '.eslintrc' ),
		} ),
	],
} );

// Javascript - Compile JS
mix.js( 'src/js/*.jsx', '/js/' ).react();

// Always sourcemaps!
// Add sourcemaps with different approaches for dev and production.
mix.sourceMaps( false, 'source-map', 'source-map' );
