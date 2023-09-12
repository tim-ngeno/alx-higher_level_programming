# JavaScript: Objects, Scopes, Closures

This README covers essential JavaScript concepts related to objects, classes, prototypes, closures, `this`, and inheritance. It provides an overview into Object Oriented JavaScript.

## Table of Contents

- [Creating Objects in JavaScript](#creating-objects-in-javascript)
- [Understanding `this` and `self`](#understanding-this-and-self)
- [The Importance of Variable Type and Scope](#importance-of-variable-type-and-scope)
- [What is Undefined in JavaScript?](#what-is-undefined)
- [Closures in JavaScript](#closures-in-javascript)
- [Understanding Prototypes](#understanding-prototypes)
- [Object-Oriented JavaScript with Classes](#object-oriented-javascript-with-classes)
- [Inheritance in JavaScript](#inheritance-in-javascript)

## Creating Objects in JavaScript

Objects are fundamental data structures that allow you to group related data and/or functions together. You can create objects using object literals:

```javascript
const person = {
  name: "John",
  age: 30,
  isStudent: false,
};
```
Here `person` is an object with the properties `name`, `age`, and a boolean value to represent whether or not `person` is a student (`isStudent`)

## Understanding `this` and `self`

In JavaScript, `this` refers to the current execution context, and it can change its value depending on how a function is called. 

Esentially, `this` binds the data it's referencing to the object that calls it

Here's an example of how `this` works in a method of an object:

```javascript
const myObject = {
  value: 42,
  getValue: function() {
    return this.value;
  },
};

console.log(myObject.getValue()); // Outputs: 42
```

## The Importance of Variable Type and Scope

Variable type (e.g., string, number, object) and scope (global or local) are crucial concepts in JavaScript as they impact how variables behave and are accessible within your code. 

Here's an example illustrating variable scope:

```javascript
let globalVar = "I'm global";

function scopeExample() {
  let localVar = "I'm local";
  console.log(globalVar); // Accessible
  console.log(localVar);  // Accessible
}

scopeExample();
console.log(globalVar); // Accessible
console.log(localVar);  // Throws an error
```

## What is Undefined in JavaScript?

`undefined` is a special value that indicates a variable has been declared but not assigned a value. It can also be returned by functions that lack a `return` statement. 

Here's an example demonstrating the concept of `undefined`:

```javascript
let myVar;
console.log(myVar); // Outputs: undefined

function noReturn() {
  // Implicitly returns undefined
}

console.log(noReturn()); // Outputs: undefined
```

# Closures in JavaScript

Closures are functions that remember the scope in which they were created, even after that scope has exited. They are a powerful concept in JavaScript and are often used for data encapsulation and private variables.

Here's an example of a closure:

```javascript
function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

const counter = createCounter();
console.log(counter()); // Outputs: 1
console.log(counter()); // Outputs: 2
```

## Understanding Prototypes

In JavaScript, all objects have a prototype, which is an object from which they inherit properties and methods. Understanding prototypes is essential for grasping how inheritance works in JavaScript.

Here's an example demonstrating prototype-based inheritance:

```javascript
const animal = {
  speak: function() {
    console.log("Animal speaks.");
  },
};

const dog = Object.create(animal);
dog.speak(); // Outputs: Animal speaks.
```

## Object-Oriented JavaScript with Classes

ES6 introduced class syntax, which provides a more structured way to create objects and define their behavior. It's a powerful tool for building object-oriented JavaScript applications.

Here's an example of defining and using a class:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

const john = new Person("John", 30);
john.greet(); // Outputs: Hello, my name is John
```

## Inheritance in JavaScript

Inheritance allows you to create a hierarchical relationship between classes, enabling one class to inherit properties and methods from another. This is a fundamental concept in object-oriented programming.

Here's an example of inheritance in JavaScript using the `extends` keyword:

```javascript
class Student extends Person {
  constructor(name, age, studentId) {
    super(name, age);
    this.studentId = studentId;
  }
}

const jane = new Student("Jane", 25, "S12345");
jane.greet(); // Outputs: Hello, my name is Jane
console.log(jane.studentId); // Outputs: S12345
```

---