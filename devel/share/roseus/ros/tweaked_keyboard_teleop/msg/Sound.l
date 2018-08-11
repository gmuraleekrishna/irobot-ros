;; Auto-generated. Do not edit!


(when (boundp 'tweaked_keyboard_teleop::Sound)
  (if (not (find-package "TWEAKED_KEYBOARD_TELEOP"))
    (make-package "TWEAKED_KEYBOARD_TELEOP"))
  (shadow 'Sound (find-package "TWEAKED_KEYBOARD_TELEOP")))
(unless (find-package "TWEAKED_KEYBOARD_TELEOP::SOUND")
  (make-package "TWEAKED_KEYBOARD_TELEOP::SOUND"))

(in-package "ROS")
;;//! \htmlinclude Sound.msg.html


(defclass tweaked_keyboard_teleop::Sound
  :super ros::object
  :slots (_sound ))

(defmethod tweaked_keyboard_teleop::Sound
  (:init
   (&key
    ((:sound __sound) 0)
    )
   (send-super :init)
   (setq _sound (round __sound))
   self)
  (:sound
   (&optional __sound)
   (if __sound (setq _sound __sound)) _sound)
  (:serialization-length
   ()
   (+
    ;; uint8 _sound
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _sound
       (write-byte _sound s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _sound
     (setq _sound (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get tweaked_keyboard_teleop::Sound :md5sum-) "e311aa13fbaf5cd07833ae9e8811de43")
(setf (get tweaked_keyboard_teleop::Sound :datatype-) "tweaked_keyboard_teleop/Sound")
(setf (get tweaked_keyboard_teleop::Sound :definition-)
      "uint8 sound
")



(provide :tweaked_keyboard_teleop/Sound "e311aa13fbaf5cd07833ae9e8811de43")


