
(cl:in-package :asdf)

(defsystem "tweaked_keyboard_teleop-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Sound" :depends-on ("_package_Sound"))
    (:file "_package_Sound" :depends-on ("_package"))
  ))