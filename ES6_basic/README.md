# ES6 Basic

This project contains exercises and examples for learning ES6 (ECMAScript 2015) features and syntax.

## Prerequisites

- Node.js (version 12 or higher)
- npm (Node Package Manager)

## Installation

1. Clone the repository and navigate to the ES6_basic directory:
   ```bash
   cd holbertonschool-web_back_end/ES6_basic
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

## Project Structure

```
ES6_basic/
├── 0-constants.js          # ES6 const and let examples
├── babel.config.js         # Babel configuration
├── package.json           # Project dependencies and scripts
├── nodesource_setup.sh    # Node.js setup script
└── README.md             # This file
```

## Configuration

### Babel Configuration
The project uses Babel to transpile ES6 code to be compatible with older JavaScript environments. The configuration is in `babel.config.js` and uses:
- `@babel/preset-env`: Automatically determines the Babel plugins and polyfills needed

### Package.json Scripts
- `npm run dev <file>`: Run a JavaScript file using babel-node
- `npm run build`: Transpile all files to the `dist` directory
- `npm run lint`: Run ESLint to check code quality

## Usage

### Running ES6 Files
To run any ES6 JavaScript file in this project:

```bash
npm run dev <filename>
```

Example:
```bash
npm run dev 0-constants.js
```

### Building for Production
To transpile all ES6 files to ES5 for production:

```bash
npm run build
```

### Code Linting
To check your code for style and potential errors:

```bash
npm run lint
```

## ES6 Features Covered

### 0-constants.js
- **const**: Block-scoped constants
- **let**: Block-scoped variables
- **export**: ES6 module exports

Example functions:
- `taskFirst()`: Demonstrates const usage
- `getLast()`: Simple function return
- `taskNext()`: Demonstrates let and string concatenation

## Dependencies

### Development Dependencies
- `@babel/cli`: Babel command line interface
- `@babel/core`: Babel core functionality
- `@babel/node`: Babel Node.js CLI
- `@babel/preset-env`: Smart preset for modern JavaScript
- `eslint`: JavaScript linting utility

## Troubleshooting

### Common Issues

1. **"Unexpected end of JSON input" error**
   - Ensure `package.json` is not empty and contains valid JSON

2. **"babel-node: command not found"**
   - Run `npm install` to install dependencies
   - Make sure you're using `npm run dev` instead of calling `babel-node` directly

3. **ES6 syntax errors**
   - Ensure `babel.config.js` is properly configured
   - Check that all required Babel presets are installed

## Learning Objectives

By working through this project, you will learn:
- The difference between `const`, `let`, and `var`
- Block scoping in ES6
- ES6 module system (import/export)
- How to set up a modern JavaScript development environment
- Using Babel to transpile ES6 code

## Author

Holberton School Web Back-End Curriculum

## License

ISC 