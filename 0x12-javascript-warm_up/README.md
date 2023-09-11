# 0x12-JavaScript

## Overview
This is a comprehensive introduction to JavaScript, covering a range of fundamental topics and basics.

## Why JavaScript is Amazing

JavaScript is amazing for several reasons:
- It's the language of the web, enabling dynamic and interactive web applications.
- It's versatile and can be used for both front-end (browser) and back-end (server) development.
- It has a large and active community, with numerous libraries and frameworks.
- It's relatively easy to learn.

## Running a JavaScript Script

To run a JavaScript script, follow these steps:
1. Create a `.js` file (e.g., `script.js`).
2. Open a terminal and navigate to the folder containing the script.
3. Use the Node.js runtime to execute the script(Make sure you have `node.js` installed) :
`node script.js`.

## Variables and Constants

In JavaScript, you can create variables using `var`, `let`, or `const`.
- `var` is function-scoped and can be redeclared.
- `let` is block-scoped and allows reassignment.
- `const` is block-scoped and immutable (its value can't change).

## Data Types in JavaScript

JavaScript has various data types, including:
- Primitive types: `number`, `string`, `boolean`, `null`, `undefined`, `bigint`, and `symbol`.
- Complex types: `object` (including arrays and functions).

## Conditional Statements

JavaScript supports conditional statements:
- `if` statements for basic condition checking.
- `if ... else` statements for branching logic.

It is also possible to nest `if .. else if ..else` statements for multiple conditions.

## Comments

You can add comments in JavaScript using `//` for single-line comments and `/* ... */` for multi-line comments.

## Working with Variables

Assign values to variables using the `=` operator. Example: `let name = "John";`.

## Loops

JavaScript offers `while` and `for` loops for iteration.
- `while` loops continue as long as a condition is true.
- `for` loops provide more control with initialization, condition, and increment parts.

## Control Statements

- `break` is used to exit a loop prematurely.
- `continue` is used to skip the current iteration and continue to the next one in a loop.

## Functions

Functions in JavaScript are blocks of reusable code. You define them using `function`. Example:
```javascript
function greet(name) {
  console.log("Hello, " + name + "!");
}
```

## Functions without a Return Statement

A function that doesn't have a `return` statement returns `undefined` by default.

## Scope of Variables

Variables in JavaScript have function-level or block-level scope. Variables declared inside a function are only accessible within that function, while those declared with `let` or `const` have block-level scope.

## Arithmetic Operators

JavaScript supports various arithmetic operators like `+`, `-`, `*`, `/`, `%`, and `**` (exponentiation).

## Working with Objects (Dictionaries)

Objects in JavaScript are collections of key-value pairs. Example:
```javascript
const person = {
  name: "Alice",
  age: 30,
};
```

## Importing Files

To import files or modules in JavaScript, you can use `import` and `require` (in Node.js).

---

