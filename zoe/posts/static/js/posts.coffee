jQuery ->
    ($ '.post-photo-link').click ->
        findPost = (post_id) ->
            for post in posts
                if post.id == post_id
                    return post

        findPhotoWithIndex = (photo_id) ->
            for photo, i in post.photos
                if photo.id == photo_id
                    return [photo, i]

        $this = ($ this)
        [post_id, photo_id] = [($this.data 'post'), ($this.data 'photo')]
        post = findPost post_id
        [photo, photo_index] = findPhotoWithIndex photo_id

        $modal = ($ (templates.post_modal.render post, photo_modal: templates.photo_modal))
        $modal.bind 'hide', ->
            $modal.remove()
        $modal.show_photo = ->
            ($modal.find 'ul.media-grid li').addClass 'hide'
            selected_photo = post.photos[photo_index]
            ($ "#photo-modal-#{selected_photo.id}").removeClass 'hide'
            ($modal.find '.index-text').text "#{photo_index + 1} of #{post.photos.length}"
            if photo_index + 1 == post.photos.length
                ($ "#post-modal-#{post.id}-next").addClass 'disabled'
            else
                ($ "#post-modal-#{post.id}-next").removeClass 'disabled'
            if photo_index == 0
                ($ "#post-modal-#{post.id}-prev").addClass 'disabled'
            else
                ($ "#post-modal-#{post.id}-prev").removeClass 'disabled'

        $modal.modal keyboard: true, backdrop: true, show: true
        ($ "#post-modal-#{post.id}-next").click ->
            if photo_index + 1 < post.photos.length
                photo_index += 1
                $modal.show_photo()
        ($ "#post-modal-#{post.id}-prev").click ->
            if photo_index > 0
                photo_index -= 1
                $modal.show_photo()

        $modal.show_photo()
        ($ '.container').append $modal

        false
