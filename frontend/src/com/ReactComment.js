import React from "react";

export default function Comment(props) {
  const url =
    "https://api.adorable.io/avatars/48/" +
    props.comment.author_name +
    "@adorable.io.png";
  console.log(props);
  return (
    <ul className="collection">
      <li className="collection-item avatar">
        <img src={url} alt="" class="circle" />
        <span className="title blue-text">{props.comment.author_name} </span>
        <p>
          <div className="media-body p-2 shadow-sm rounded bg-light border">
            {props.comment.content}
          </div>
        </p>
      </li>
    </ul>
  );
}
