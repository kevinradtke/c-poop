import React from "react";
import { List, ListSubheader } from "@material-ui/core/";
import _ from "lodash";
import EmojiItemButton from "./emoji-item-button/EmojiItemButton";
import EMOJI_CATEGORIES from "../../../constants/emoji-categories";
import useStyles from "./emoji-pane.jss";

const EmojiList = () => {
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
                  <EmojiItemButton
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
};

export default EmojiList;
