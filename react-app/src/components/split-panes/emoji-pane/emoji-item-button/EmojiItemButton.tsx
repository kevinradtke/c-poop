import React, { useContext } from "react";
import {
  Avatar,
  ListItem,
  ListItemAvatar,
  ListItemText,
  Typography
} from "@material-ui/core/";
import { CodeContext } from "../../../../contexts";

import useStyles from "./emoji-item-button.jss";

interface Props {
  sectionId: string;
  emoji: string;
  equivalentValue: string;
  shortcode?: string;
}

const EmojiItemButton: React.FC<Props> = (props: Props) => {
  const { sectionId, emoji, equivalentValue } = props;
  const { addEmoji } = useContext(CodeContext);

  const classes = useStyles();
  return (
    <ListItem
      button
      key={`item-${sectionId}-${emoji}`}
      className={classes.nested}
      onClick={() => addEmoji(emoji)}
    >
      <ListItemAvatar>
        <Avatar className={classes.avatar}>
          <span> {emoji}</span>
        </Avatar>
      </ListItemAvatar>
      <ListItemText
        primary={
          <Typography style={{ fontSize: "18px" }}>
            {equivalentValue}
          </Typography>
        }
      />
    </ListItem>
  );
};

export default EmojiItemButton;
