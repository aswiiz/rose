const gifts={
 hug:['assets/gift-hug.gif','A warm little kitty hug, just for you. If I could, I’d give you one right now. ♡'],
 flowers:['assets/gift-flowers.gif','A tiny bouquet to remind you that you make my days bloom. 💐'],
 chocolate:['assets/gift-chocolate.gif','Something sweet for someone who makes life sweeter. 🍫'],
 teddy:['assets/gift-teddy.gif','A soft virtual cuddle for whenever you need one. 🧸'],
 wish:['assets/gift-wish.gif','A little wish: may we keep finding reasons to smile together. 💌']
};
document.querySelectorAll('.gift').forEach(btn=>btn.addEventListener('click',()=>{
 const [url,msg]=gifts[btn.dataset.gift];
 const gif=document.getElementById('giftGif');
 if(gif) gif.src=url;
 const message=document.getElementById('giftMessage');
 if(message) message.textContent=msg;
 const reveal=document.getElementById('giftReveal');
 if(reveal) reveal.hidden=false;
}));
const close=document.getElementById('closeGift');
if(close) close.addEventListener('click',()=>{
 const reveal=document.getElementById('giftReveal'); if(reveal) reveal.hidden=true;
 const gif=document.getElementById('giftGif'); if(gif) gif.src='assets/gift-hug.gif';
});
const yes=document.getElementById('yesBtn');
if(yes) yes.addEventListener('click',()=>{
 const a=document.getElementById('answer');
 if(a) a.textContent='You made me so happy, Pavithra. Thank you for choosing to begin this with me. I’m looking forward to all the little memories we’ll make together. ❤️';
});
const time=document.getElementById('timeBtn');
if(time) time.addEventListener('click',()=>{
 const a=document.getElementById('answer');
 if(a) a.textContent='Of course, Pavithra. Take all the time you need. I care about you, and I want you to feel comfortable being honest with me. ❤️';
});
