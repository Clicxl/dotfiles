import { JSXElementConstructor } from "react";

export default function loaderInput():JSXElementConstructor {
  return (
    <div className="loaderInput">
      <input type="text" name="loader" id="loader" />
    </div>
  )
}
