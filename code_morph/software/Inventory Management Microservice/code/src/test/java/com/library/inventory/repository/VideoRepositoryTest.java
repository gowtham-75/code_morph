```java
package com.library.inventory.repository;

import com.library.inventory.model.Video;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
public class VideoRepositoryTest {

    @Autowired
    private VideoRepository videoRepository;

    private Video video;

    @BeforeEach
    public void setup() {
        video = new Video();
        video.setTitle("The Matrix");
        video.setDirector("Lana Wachowski, Lilly Wachowski");
        video.setGenre("Science Fiction");
        video.setLocationId("1");
        video.setBranchId("1");
    }

    @Test
    public void whenSaveVideo_thenShouldBeAbleToFetchIt() {
        video = videoRepository.save(video);
        Optional<Video> fetchedVideo = videoRepository.findById(video.getId());
        assertThat(fetchedVideo).isPresent();
        assertThat(fetchedVideo.get()).isEqualToComparingFieldByField(video);
    }

    @Test
    public void whenDeleteVideo_thenShouldNotBeAbleToFetchIt() {
        video = videoRepository.save(video);
        videoRepository.deleteById(video.getId());
        Optional<Video> fetchedVideo = videoRepository.findById(video.getId());
        assertThat(fetchedVideo).isNotPresent();
    }

    @Test
    public void whenUpdateVideo_thenShouldReflectChanges() {
        video = videoRepository.save(video);
        Video updatedVideo = new Video();
        updatedVideo.setId(video.getId());
        updatedVideo.setTitle("The Matrix Reloaded");
        updatedVideo.setDirector(video.getDirector());
        updatedVideo.setGenre(video.getGenre());
        updatedVideo.setLocationId(video.getLocationId());
        updatedVideo.setBranchId(video.getBranchId());

        videoRepository.save(updatedVideo);

        Optional<Video> fetchedVideo = videoRepository.findById(video.getId());
        assertThat(fetchedVideo).isPresent();
        assertThat(fetchedVideo.get().getTitle()).isEqualTo("The Matrix Reloaded");
    }
}
```