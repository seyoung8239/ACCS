import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function BoardCard({post}) {
  return (
    <Card sx={{ minWidth: 275 }} variant="outlined">
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          {post.location}
        </Typography>
        <Typography variant="h5" component="div">
          {post.title}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {post.date}
        </Typography>
        <Typography variant="body2">
          {post.content}
        </Typography>
      </CardContent>
    </Card>
  );
}
