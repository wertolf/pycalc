# Python and PyQt: Building a GUI Desktop Calculator

https://realpython.com/python-pyqt-gui-calculator/

## Getting to Know PyQt

In this tutorial, you’ll use PyQt6, as this version is the future of the library. From now on, be sure to consider any mention of PyQt as a reference to PyQt6.

PyQt and PySide are both built on top of Qt. Their APIs are quite similar because they reflect the Qt API. That’s why porting PyQt code to PySide can be as simple as updating some imports. If you learn one of them, then you’ll be able to work with the other with minimal effort.

## Installing PyQt

### Virtual Environment Installation With pip

less than 100 MBs' network bandwidth

### System-Wide Installation With pip

### Platform-Specific Installation

If you use a package manager on Linux or macOS, then there’s a chance you won’t get the latest version of PyQt6. A pip installation will be better if you want to ensure that you have the latest release.

## Creating Your First PyQt Application

You should create your app instance before you create any GUI object in PyQt.

You can use .setGeometry() to define the window’s size and screen position. The first two arguments are the x and y screen coordinates where the window will be placed. The third and fourth arguments are the window’s width and height.

要实现窗口的居中显示，只需要获得屏幕的宽度和高度，然后与窗口的宽度和高度进行计算即可

In PyQt, you can use any widget—a subclass of QWidget—as a top-level window. The only condition is that the target widget must not have a parent widget. When you use a widget as your top-level window, PyQt automatically provides it with a title bar and turns it into a normal window.

The **parent-child relationship** between widgets has two complementary purposes. A widget with no parent is considered a main or **top-level window**. In contrast, a widget with an explicit parent is a **child widget**, and it’s shown within its parent.

This relationship is also known as **ownership**, with parents owning their children. The PyQt ownership model ensures that if you delete a parent widget, such as your top-level window, then all of its child widgets will automatically be deleted as well.

To avoid memory leaks, you should always make sure that any QWidget object has a parent, with the sole exception of your top-level windows.

## Considering Code Styles

If you check the code of your sample GUI application from the previous section, then you’ll notice that PyQt’s API doesn’t follow PEP 8 coding style and naming conventions. PyQt is built around Qt, which is written in C++ and uses the camel case naming style for functions, methods, and variables.

In this regard, PEP 8 states that:
> New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

In addition, the Zen of Python says:
> ... practicality beats purity.

If you want to write consistent PyQt-related code, then you should stick to the framework’s coding style. In this tutorial, you’ll follow the PyQt coding style for consistency. You’ll use camel case instead of the usual Python snake case.

## Learning the Basics of PyQt

You’ll need to master the basic components of PyQt if you want to proficiently use this library to develop your GUI applications. Some of these components include:

* Widgets
* Layout managers
* Dialogs
* Main windows
* Applications
* Event loops
* Signals and slots

### Widgets

Some of the most common and useful PyQt widgets are:

* Buttons
* Labels
* Line edits
* Combo boxes
* Radio buttons

### Layout Managers

The most effective and recommended technique is to use PyQt’s layout managers. They’ll increase your productivity, mitigate the risk of errors, and improve your code’s maintainability.

### Dialogs

Dialogs with a parent will share the parent’s task bar entry. If you don’t set parent for a given dialog, then the dialog will get its own entry in the system’s task bar.

You can nest layouts by calling .addLayout() on the container layout with the nested layout as an argument.

### Main Windows

Up to this point, you’ve learned about some of the more important graphical components in PyQt’s set of widgets. In the next few sections, you’ll study other important concepts related to building GUI applications with PyQt.

### Applications

Every PyQt GUI application must have one QApplication instance. Some of the responsibilities of this class include:

* Handling the app’s initialization and finalization
* Providing the **event loop** and event handling
* Handling most system-wide and application-wide settings
* Providing access to **global information**, such as the application’s directory, screen size, and so on
* Parsing common command-line arguments
* Defining the application’s look and feel
* Providing localization capabilities

### Event Loops

GUI applications are **event-driven**. This means that functions and methods are called in response to user actions, like clicking on a button, selecting an item from a combo box, entering or updating the text in a text edit, pressing a key on the keyboard, and so on. These user actions are commonly known as **events**.

question: what's the relationship between **events** and **interrupts**

Events are handled by an **event loop**, also known as a **main loop**. An event loop is an infinite loop in which all events from the user, the window system, and any other sources are processed and dispatched. The event loop waits for an event to occur and then dispatches it to perform some task. The event loop continues to work until the application is terminated.

All GUI applications have an event loop. When an event happens, then the loop checks if it’s a **terminate event**. In that case, the loop finishes, and the application exits. Otherwise, the event is sent to the application’s event queue for further processing, and the loop iterates again. In PyQt6, you can run the app’s event loop by calling .exec() on the QApplication object.

For an event to trigger an action, you need to connect the event with the action that you want to execute. In PyQt, you can establish that connection with the signals and slots mechanism, which you’ll explore in the next section.

### Signals and Slots

PyQt widgets act as **event-catchers**. This means that every widget can catch specific events, like mouse clicks, keypresses, and so on. In response to these events, a widget emits a **signal**, which is a kind of message that announces a change in its state.

The signal on its own doesn’t perform any action. If you want a signal to trigger an action, then you need to connect it to a **slot**. This is the function or method that’ll perform an action whenever its associated signal is emitted. You can use any Python **callable** as a slot.


If your slot function needs to receive extra arguments, then you can pass them using functools.partial().


The signals and slots mechanism is what you’ll use to give life to your PyQt GUI applications. This mechanism will allow you to turn user events into concrete actions. You can dive deeper into signals and slots by checking out the PyQt6 documentation on the topic.

https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html

## Creating a Calculator App With Python and PyQt

The MVC design pattern has 3 layers of code:

The **model** takes care of your app’s business logic. It contains the core functionality and data. In your calculator app, the model will handle the input values and the calculations.

The **view** implements your app’s GUI. It hosts all the widgets that the end user would need to interact with the application. **The view also receives a user’s actions and events.** For your example, the view will be the calculator window on your screen.

The **controller** connects the model and the view to make the application work. Users’ events, or requests, are sent to the controller, which puts the model to work. When the model delivers the requested result, or data, in the right format, the controller forwards it to the view.

In your calculator app, the controller will
* receive the target math expressions from the GUI,
* ask the model to perform calculations,
* and update the GUI with the result.

### Creating the Skeleton for Your PyQt Calculator App

### Completing the App’s View

To represent a coordinate pair, you’ll use a list of lists.
Each nested list will represent a row.


When it comes to widget size, you’ll rarely find measurement units in the PyQt documentation. The measurement unit is assumed to be **pixels**, except when you’re working with QPrinter class, which uses **points**.


When the user clicks the equal sign (=) on the calculator’s keyboard, the app will use the return value of .displayText() as the math expression to be evaluated.

### Implementing the Calculator’s Model

我还纳闷这个计算器的 business logic 是怎么实现的，原来是直接偷懒调用了内置的 exec 函数，哈哈

The `evaluateExpress` function has a couple of important issues:
* The try … except block doesn’t catch a specific exception,
  so it’s using a practice that’s discouraged in Python.
* The function uses eval(), which can lead to some serious security issues.

https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html

You’re free to rework the function to make it more reliable and secure.
In this tutorial,
you’ll use the function as is to keep the focus on implementing the GUI.

### Creating the Controller Class for Your Calculator

The controller class will connect the view to the model that you just coded.
You’ll use it to make the calculator perform actions in response to user events.

Your controller class needs to perform three main tasks:

* Access the GUI’s public interface.
* Handle the creation of math expressions.
* Connect all the buttons’ .clicked signals with the appropriate slots.

### Running the Calculator

## Additional Tools

Qt Designer allows you to design and build graphical user interfaces using a drag-and-drop interface. You can use this tool to design widgets, dialogs, and main windows by using on-screen forms and a drag-and-drop mechanism.

Qt Designer uses XML .ui files to store your GUI designs. PyQt includes a module called uic to help with .ui files. You can also convert the .ui file content into Python code with a command-line tool called pyuic6.

C# 里面也是用 XAML 定义页面的布局

可见使用 XML 或类似的标记语言存储页面布局信息是一个业界通用的 practice

## Conclusion

## Further Reading
