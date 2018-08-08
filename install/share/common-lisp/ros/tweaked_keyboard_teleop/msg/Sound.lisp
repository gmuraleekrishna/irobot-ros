; Auto-generated. Do not edit!


(cl:in-package tweaked_keyboard_teleop-msg)


;//! \htmlinclude Sound.msg.html

(cl:defclass <Sound> (roslisp-msg-protocol:ros-message)
  ((sound
    :reader sound
    :initarg :sound
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Sound (<Sound>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sound>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sound)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tweaked_keyboard_teleop-msg:<Sound> is deprecated: use tweaked_keyboard_teleop-msg:Sound instead.")))

(cl:ensure-generic-function 'sound-val :lambda-list '(m))
(cl:defmethod sound-val ((m <Sound>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tweaked_keyboard_teleop-msg:sound-val is deprecated.  Use tweaked_keyboard_teleop-msg:sound instead.")
  (sound m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sound>) ostream)
  "Serializes a message object of type '<Sound>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'sound)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sound>) istream)
  "Deserializes a message object of type '<Sound>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'sound)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sound>)))
  "Returns string type for a message object of type '<Sound>"
  "tweaked_keyboard_teleop/Sound")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sound)))
  "Returns string type for a message object of type 'Sound"
  "tweaked_keyboard_teleop/Sound")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sound>)))
  "Returns md5sum for a message object of type '<Sound>"
  "e311aa13fbaf5cd07833ae9e8811de43")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sound)))
  "Returns md5sum for a message object of type 'Sound"
  "e311aa13fbaf5cd07833ae9e8811de43")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sound>)))
  "Returns full string definition for message of type '<Sound>"
  (cl:format cl:nil "uint8 sound~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sound)))
  "Returns full string definition for message of type 'Sound"
  (cl:format cl:nil "uint8 sound~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sound>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sound>))
  "Converts a ROS message object to a list"
  (cl:list 'Sound
    (cl:cons ':sound (sound msg))
))
