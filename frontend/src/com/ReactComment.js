import React from "react";

export default function Comment(props) {
  const { message} = props.comment;
  const url =
      "https://api.adorable.io/avatars/48/uu@adorable.io.png"

  return (

    <ul className="collection">
                <li className="collection-item avatar">
                <img src={url} alt="" class="circle" />
                    <span className="title blue-text">username </span>
                    <p><div className="media-body p-2 shadow-sm rounded bg-light border">
        {/* <small className="float-right text-muted">{time}</small> */}
        {/* <h6 className="mt-0 mb-1 text-muted">{name}</h6> */}
        {message}
      </div>
      </p>
                </li>
            </ul>
  );
}
