import React from "react";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import ListSubheader from "@material-ui/core/ListSubheader";

import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";

import Typography from "@material-ui/core/Typography";

import _ from "lodash";

import EMOJI_CATEGORIES from "../../../constants/emoji-categories";

import useStyles from "./EmojiPane.jss";

interface Props {
  // List Props
  sectionId: string;
  // Emoji Props
  emoji: string;
  equivalentValue: string;
  shortcode: string;
}

const Item: React.FC<Props> = (props: Props) => {
  const { sectionId, emoji, equivalentValue } = props;
  const classes = useStyles();
  return (
    <ListItem
      button
      key={`item-${sectionId}-${emoji}`}
      className={classes.nested}
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

export default function PinnedSubheaderList() {
  const classes = useStyles();

  return (
    <List className={classes.root} subheader={<li />}>
      {EMOJI_CATEGORIES.map(emojiCategory => {
        const [[categoryName, emojiArray]] = Object.entries(emojiCategory);

        return (
          <li key={`section-${categoryName}`} className={classes.listSection}>
            <ul className={classes.ul}>
              <ListSubheader>{_.startCase(categoryName)}</ListSubheader>
              {emojiArray.map(emojiObj => {
                const { emoji, equivalentValue, shortcode } = emojiObj;

                return (
                  <Item
                    key={`item-${categoryName}-${shortcode}`}
                    sectionId={emojiCategory.toString()}
                    emoji={emoji}
                    equivalentValue={equivalentValue}
                    shortcode={shortcode}
                  />
                );
              })}
            </ul>
          </li>
        );
      })}
    </List>
  );
}
