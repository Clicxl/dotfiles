import {
  element_usernameInput,
  element_emailInput,
  element_passwordInput,
  element_submitButton,
} from "./CONSTANTS";
import { formConfigType } from "./types";

let element_usernameInput = element_usernameInput as HTMLElement;

let usernameHasError: boolean = false;
element_usernameInput.addEventListener("input", () => {
  // When username field changes...

  // Test if the value of the username input field won't be accepted.

  // 3-25 characters in length.
  // Accepted characters: A-Z 0-9
  // Doesn't contain existing/reserved usernames.
  // Doesn't contain profain words.

  let usernameError: HTMLElement | null =
    document.getElementById("usernameerror"); // Does an error already exist?

  const lengthError = element_usernameInput.value.length < 3;
  const formatError = !onlyLettersAndNumbers(element_usernameInput.value);

  // If ANY error, make sure errorElement is created
  if ((lengthError || formatError) && !usernameError) {
    // merged the if condition
    // Create empty errorElement
    usernameHasError = true;
    createErrorElement("usernameerror", "usernameinputline");
    // Change input box to red outline
    element_usernameInput.style.outline = "solid 1px red";
    // Reset variable because it now exists.
    usernameError = document.getElementById("usernameerror");
  } else if (usernameError) {
    // No errors, delete that error element if it exists
    usernameHasError = false;
    usernameError.remove();
    element_usernameInput.removeAttribute("style");
  }

  if (usernameError instanceof HTMLElement) {
    if (lengthError && formatError) {
      // Change error message
      usernameError.textContent =
        "Username must be atleast 3 characters long, and only contain letters A-Z and numbers 0-9";
    } else if (lengthError) {
      usernameError.textContent = "Username must be atleast 3 characters long";
    } else if (formatError) {
      usernameError.textContent =
        "Username must only contain letters A-Z and numbers 0-9";
    }
  }

  updateSubmitButton();
});
element_usernameInput.addEventListener("focusout", () => {
  // Check username availability...
  if (element_usernameInput.value.length === 0 || usernameHasError) return;

  fetch(`/createaccount/username/${element_usernameInput.value}`)
    .then((response) => response.json())
    .then((result) => {
      // { allowed, reason }
      // We've got the result back from the server,
      // Is this username available to use?
      if (result.allowed === true) return; // Not in use

      // redeclaring the variable
      let usernameError: HTMLElement | null =
        document.getElementById("usernameerror");

      // ERROR! In use!
      usernameHasError = true;
      createErrorElement("usernameerror", "usernameinputline");
      // Change input box to red outline
      element_usernameInput.style.outline = "solid 1px red";
      // Reset variable because it now exists.
      usernameError = document.getElementById("usernameerror");

      if (usernameError instanceof HTMLElement) {
        usernameError.textContent = result.reason;
        updateSubmitButton();
      }
    });
});

let emailHasError = false;
element_emailInput.addEventListener("input", () => {
  // When email field changes...

  // Test if the email is a valid email format

  let emailError: HTMLElement | null = document.getElementById("emailerror"); // Does an error already exist?

  const error = !validEmail(element_emailInput.value);

  // If ANY error, make sure errorElement is created
  if (error) {
    if (!emailError) {
      // Create empty errorElement
      emailHasError = true;
      createErrorElement("emailerror", "emailinputline");
      // Change input box to red outline
      element_emailInput.style.outline = "solid 1px red";
      // Reset variable because it now exists.
      emailError = document.getElementById("emailerror");
    }
  } else if (emailError) {
    // No errors, delete that error element if it exists
    emailHasError = false;
    emailError.remove();
    element_emailInput.removeAttribute("style");
  }

  if (error && emailError) {
    emailError.textContent = "This is not a valid email";
  }

  updateSubmitButton();
});
element_emailInput.addEventListener("focusout", () => {
  // Check email availability...
  // If it's blank, all the server would send back is the createaccount.html again..

  if (element_emailInput.value.length > 1 && !emailHasError) {
    fetch(`/createaccount/email/${element_emailInput.value}`)
      .then((response) => response.json())
      .then((result) => {
        // We've got the result back from the server,
        // Is this email available to use?
        if (result[0] === false) {
          // Email in use
          emailHasError = true;

          createErrorElement("emailerror", "emailinputline");
          // Change input box to red outline
          element_emailInput.style.outline = "solid 1px red";
          // Reset variable because it now exists.
          const emailError = document.getElementById("emailerror");
          if (emailError instanceof HTMLElement) {
            emailError.textContent = "This email is already in use";
            updateSubmitButton();
          }
        }
      });
  }
});

let passwordHasError = false;
element_passwordInput.addEventListener("input", () => {
  // When password field changes...

  let passwordError: HTMLElement | null =
    document.getElementById("passworderror"); // Does an error already exist?

  const shortError = element_passwordInput.value.length < 6;
  const longError = element_passwordInput.value.length > 72;
  const formatError = !validPassword(element_passwordInput.value);
  const containsPasswordError =
    element_passwordInput.value.toLowerCase() === "password";

  // If ANY error, make sure errorElement is created
  if (shortError || longError || formatError || containsPasswordError) {
    if (!passwordError) {
      // Create empty errorElement
      passwordHasError = true;
      createErrorElement("passworderror", "passwordinputline");
      // Change input box to red outline
      element_passwordInput.style.outline = "solid 1px red";
      // Reset variable because it now exists.
      passwordError = document.getElementById("passworderror");
    }
  } else if (passwordError) {
    // No errors, delete that error element if it exists
    passwordHasError = false;
    passwordError.remove();
    element_passwordInput.removeAttribute("style");
  }

  if (passwordError instanceof HTMLElement) {
    if (formatError) {
      passwordError.textContent = "Password is in an incorrect format";
    } else if (shortError) {
      passwordError.textContent = "Password must be 6+ characters long";
    } else if (longError) {
      passwordError.textContent = "Password can't be over 72 characters long";
    } else if (containsPasswordError) {
      passwordError.textContent = "Password must not be 'password'";
    }
  }
  updateSubmitButton();
});

element_submitButton.addEventListener("click", (event) => {
  event.preventDefault();

  if (
    !usernameHasError &&
    !emailHasError &&
    !passwordHasError &&
    element_usernameInput.value &&
    element_emailInput.value &&
    element_passwordInput.value
  )
    sendForm(
      element_usernameInput.value,
      element_emailInput.value,
      element_passwordInput.value
    );
});

/**
 * Sends our form data to the createaccount route.
 * @param {string} username
 * @param {string} email
 * @param {string} password
 */
function sendForm(username: string, email: string, password: string) {
  let OK = false;
  let config: formConfigType = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "same-origin", // Allows cookie to be set from this request
    body: JSON.stringify({ username, email, password }),
  };
  fetch("/createaccount", config)
    .then((response) => {
      if (response.ok) OK = true;
      return response.json();
    })
    .then(() => {
      if (OK) {
        // Account created!
        // We also received the refresh token cookie to start a session.
        // token = getCookieValue('token') // Cookie expires in 60s
        window.location.href = `/member/${username.toLowerCase()}`;
      } else {
        // Conflict, unable to make account. 409 CONFLICT
        window.location.href = "/409";
      }
    });
}

function createErrorElement(id: string, insertAfter: string) {
  const errElement = document.createElement("div");
  errElement.className = "error";
  errElement.id = id;
  // The element now looks like this:
  // <div class="error" id="usernameerror"></div>

  const insertAfterElement = document.querySelector(`#${insertAfter}`);
  if (insertAfterElement instanceof HTMLElement) {
    insertAfterElement.insertAdjacentElement("afterend", errElement);
  }
}

// Greys-out submit button if there's any errors.
// The click-prevention is taken care of in the submit event listener.
function updateSubmitButton(): void {
  if (
    usernameHasError ||
    emailHasError ||
    passwordHasError ||
    !element_usernameInput.value ||
    !element_emailInput.value ||
    !element_passwordInput.value
  ) {
    element_submitButton.className = "unavailable";
  } else {
    // No Errors
    element_submitButton.className = "ready";
  }
}

function onlyLettersAndNumbers(string: string): boolean | string {
  if (!string) return true;
  return /^[a-zA-Z0-9]+$/.test(string);
}

function validEmail(string: string): boolean {
  // Credit for the regex: https://stackoverflow.com/a/201378
  const regex =
    /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
  if (regex.test(string) === true) return true;
  return false;
}

function validPassword(string: string) {
  const regex = /^[a-zA-Z0-9!@#$%^&*\?]+$/;

  if (regex.test(string) === true) return true;
  return false;
}

function getCookieValue(cookieName: string): string | undefined {
  const cookieArray = document.cookie.split("; ");

  for (let i = 0; i < cookieArray.length; i++) {
    const cookiePair = cookieArray[i].split("=");

    if (cookiePair[0] === cookieName) {
      return cookiePair[1];
    }
  }
}
