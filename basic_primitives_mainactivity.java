package com.example.basic_primitives;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.drawable.BitmapDrawable;
import android.os.Bundle;
import android.widget.ImageView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Bitmap bm = Bitmap.createBitmap(720,1280,Bitmap.Config.ARGB_8888);
        ImageView i = findViewById(R.id.image);
        i.setBackgroundDrawable(new BitmapDrawable(bm));
        Canvas canvas=new Canvas(bm);
        Paint paint=new Paint();
        paint.setColor(Color.RED);
        paint.setTextSize(50);
        canvas.drawRect(400,200,600,700,paint);
        canvas.drawCircle(200,200,100,paint);
        canvas.drawRect(50,800,300,1100,paint);
        canvas.drawLine(500,800,500,1100,paint);
    }
}
